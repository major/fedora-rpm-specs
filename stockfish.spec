%global srcname  Stockfish
%global nnuehash 6877cd24400e

Name:            stockfish
Version:         15
Release:         2%{?dist}
#Source0:        %%{url}/files/%%{name}-%%{version}-linux.zip
Source0:         https://github.com/official-%{name}/%{srcname}/archive/sf_%{version}.zip
Summary:         Powerful open source chess engine
# CC0 is for the NNUE network file (see https://tests.stockfishchess.org/nns)
License:         GPLv3+ and CC0
URL:             http://%{name}chess.org

# the NN file
Source1:         https://tests.stockfishchess.org/api/nn/nn-%nnuehash.nnue

# steal some documentation from ubuntu
Source10:        https://bazaar.launchpad.net/~ubuntu-branches/ubuntu/vivid/%{name}/vivid/download/head:/engineinterface.txt-20091204230329-yljoyxocuxhxg1ot-78/engine-interface.txt#/%{name}-interface.txt
Source11:        https://bazaar.launchpad.net/~ubuntu-branches/ubuntu/vivid/%{name}/vivid/download/head:/%{name}.6-20091204230329-yljoyxocuxhxg1ot-76/%{name}.6

# polyglot support
Source20:        https://raw.githubusercontent.com/mpurland/%{name}/master/polyglot.ini#/%{name}-polyglot.ini

BuildRequires:  gcc-c++
BuildRequires:  make

#Suggests:       polyglot-chess

%description
Stockfish is a free UCI chess engine derived from Glaurung 2.1. It is not a
complete chess program, but requires some UCI compatible GUI (like XBoard with
PolyGlot, eboard, Arena, Sigma Chess, Shredder, Chess Partner or Fritz) in
order to be used comfortably. Read the documentation for your GUI of choice for
information about how to use Stockfish with your GUI.


%prep
# verify the NNUE net checksum early to catch maintainer error
test %nnuehash = "$(sha256sum %{SOURCE1} | cut -c1-12)"

#%%autosetup -n%%{name}-%%{version}-linux
%autosetup -n%{srcname}-sf_%{version}

cp -t. -p %{SOURCE10} %{SOURCE11}
cp -tsrc -p %{SOURCE1}

# W: wrong-file-end-of-line-encoding
sed -i 's,\r$,,' %{name}-interface.txt

# polyglot of installed binary and disable log
sed -e 's,\(EngineDir = \).*,\1%{_bindir},' \
 -e 's,\(EngineCommand = \).*,\1%{name},' \
 -e 's,\(LogFile = \).*,\1~/,' -e 's,\(LogFile = \).*,\1false,' \
 %{SOURCE20} >polyglot.ini


%build
# default to general-64, which also works for s390x
%global sfarch general-64

%ifarch x86_64
%global sfarch x86-64
%endif
%ifarch i686
%global sfarch x86-32
%endif
%ifarch ppc64le
%global sfarch ppc-64
%endif
%ifarch aarch64
%global sfarch armv8
%endif
%ifarch armv7hl
%global sfarch armv7
%endif

# NOTE: The upstream Makefile adds some flags on top of the Fedora ones.
# Most of them are harmless/redundant except -O3. However, benchmarks
# (based on the duration of `stockfish bench` in koji builders) support
# the use of -O3 here:
# Architecture | armv7hl | i686 | x86_64 | aarch64 | ppc64le | s390x
# -O3 speedup  |     1%% | 14%% |   13%% |    10%% |    31%% |   1%%
%if 0%{?el8}
%ifarch s390x
# (EPEL8 only):
#   during GIMPLE pass: vect
#   main.cpp: In function 'main':
#   main.cpp:33:5: internal compiler error: Segmentation fault
#    int main(int argc, char* argv[]) {
#        ^
# Reducing the optimization level fixes this at the cost of some performance;
# according to the benchmarks above, the impact is trivial on s390x anyway.
sed -r -i 's/-O3//' src/Makefile
%endif
%endif
%make_build -C src build ARCH=%sfarch \
    EXTRACXXFLAGS="%{build_cxxflags}" \
    EXTRALDFLAGS="%{build_ldflags}"


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -p src/%{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
cp -p %{name}.6 %{buildroot}%{_mandir}/man6
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -p polyglot.ini %{buildroot}%{_sysconfdir}/%{name}


%check
# run bench as a sanity check
./src/%{name} bench


%files
%license Copying.txt
%doc AUTHORS %{name}-interface.txt README.md
%{_mandir}/man*/%{name}*
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/polyglot.ini


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 19 2022 Ondrej Mosnacek <omosnace@redhat.com> - 15-1
- Bump to version 15
- Resolves: rhbz#2076750

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Ondrej Mosnacek <omosnace@redhat.com> - 14.1-1
- Adapt spec file for NNUE support
- Use upstream buildsystem
- Bump to version 14.1
- Resolves: rhbz#1875192
- Resolves: rhbz#1988004

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 06 2020 Raphael Groner <raphgro@fedoraproject.orgi> - 12-1
- bump to version 12
- use c++17 for std::clamp

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 11-4
- Do not force C++11 mode

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Raphael Groner <projects.rg@smart.ms> - 11-1
- new version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 10-1
- new version

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Raphael Groner <projects.rg@smart.ms> - 9-1
- new version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Raphael Groner <projects.rg@smart.ms> - 8-1
- new version

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-3.20160225gite1a7d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7-2.20160225gite1a7d13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 05 2016 Raphael Groner <projects.rg@smart.ms> - 7-1.20160225gite1a7d13
- bump to show official upstream release of sf_7

* Sat Mar 05 2016 Raphael Groner <projects.rg@smart.ms> - 7-0.11.20160225gite1a7d13
- new upstream snapshot

* Wed Feb 03 2016 Raphael Groner <projects.rg@smart.ms> - 7-0.10.20160118gitaedebe3
- new upstream snapshot

* Tue Dec 15 2015 Raphael Groner <projects.rg@smart.ms> - 7-0.9.20151105git76ed0ab
- new upstream snapshot

* Fri Nov 13 2015 Raphael Groner <projects.rg@smart.ms> - 7-0.8.20151105git76ed0ab
- new upstream snapshot

* Sun Oct 11 2015 Raphael Groner <projects.rg@smart.ms> - 7-0.7.20151007git55b46ff
- new upstream snapshot

* Wed Aug 19 2015 Raphael Groner <projects.rg@smart.ms> - 7-0.6.20150817git69a1a80
- new upstream tarball as of 20150817

* Wed Jul 22 2015 Raphael Groner <projects.rg@smart.ms> - 7-0.5.20150716git4095ff0
- new snapshot of upstream

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-0.4.20150506git2e86d1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Raphael Groner <projects.rg@smart.ms> - 7-0.3.20150506git2e86d1f
- latest snapshot from upstream

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 7-0.2.20150302gitcb2111f
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 02 2015 Raphael Groner <projects.rg@smart.ms> - 7-0.1.20150302gitcb2111f
- prepare next major version bump with latest upstream commit
- merged c++11 branch (upstream)
- disable spinlocks (upstream)
- favour fishtest (upstream)

* Mon Mar 02 2015 Raphael Groner <projects.rg@smart.ms> - 6-4.20150228git1e6d21d
- fix ownership of etc/
- add Suggests: polyglot-chess (rhbz#1197333)
- latest commit from upstream
- merged c++11 branch (upstream)
- disable spinlocks (upstream)
- favour fishtest (upstream)

* Sun Mar 01 2015 Raphael Groner <projects.rg@smart.ms> - 6-3.20150228git1e6d21d
- implement cmake
- harden gcc5
- latest commit from upstream

* Sat Feb 28 2015 Raphael Groner <projects.rg (AT) smart.ms> - 6-2.20150226git8a2c413
- switch to official github sources (as mentioned at homepage)
- provide polyglot support
- disable debuginfo

* Wed Feb 25 2015 Raphael Groner <projects.rg (AT) smart.ms> - 6-1.20150131gitb331768
- bump to version 6 and switch to commits

* Tue Sep 10 2013 Dhiru Kholia <dhiru@openwall.com> - 4-2
- fixed prep section and book path, removed dos2unix call, confirm to FHS
- preserve timestamps for resources, use ExclusiveArch, preserve debug symbols

* Tue Sep 10 2013 Dhiru Kholia <dhiru@openwall.com> - 4-1
- initial version based on stockfish.spec from mageia
