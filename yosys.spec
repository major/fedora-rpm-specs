%global commit0 389b8d0f94a24c30e5b9352866f0999b14312b23
%global shortcommit0 %%(c=%%{commit0}; echo ${c:0:7})

%global snapdate 20230809

%global __python %{__python3}

Name:           yosys
Version:        0.32
Release:        1.%{snapdate}git%{shortcommit0}%{?dist}
Summary:        Yosys Open SYnthesis Suite, including Verilog synthesizer
License:        ISC and MIT
URL:            http://www.clifford.at/yosys/

Source0:        https://github.com/YosysHQ/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1:        https://github.com/mdaines/viz.js/releases/download/0.0.3/viz.js

# man pages written for Debian:
Source2:        http://http.debian.net/debian/pool/main/y/yosys/yosys_0.9-1.debian.tar.xz
# requested that upstream include those man pages:
#   https://github.com/YosysHQ/yosys/issues/278

# Fedora-specific patch:
# Change the substitution done when making yosys-config so that it outputs
# CXXFLAGS with -I/usr/include/yosys
Patch1:         yosys-cfginc.patch

# Fedora-specific patch:
# When invoking yosys-config for examples in "make manual", need to use
# relative path for includes, as they're not installed in build host
# filesystem.
Patch2:         yosys-mancfginc.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  bison flex readline-devel pkgconfig
BuildRequires:  tcl-devel libffi-devel
BuildRequires:  yosyshq-abc >= 0.31
BuildRequires:  iverilog >= 12.0
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  txt2man

# required for documentation:
BuildRequires:  graphviz
BuildRequires:  texlive-beamer
BuildRequires:  texlive-collection-bibtexextra
BuildRequires:  texlive-collection-fontsextra
BuildRequires:  texlive-collection-latexextra
BuildRequires:  texlive-collection-publishers
BuildRequires:  texlive-collection-science

Requires:       %{name}-share = %{version}-%{release}
Requires:       graphviz python-xdot
Requires:       yosyshq-abc >= 0.31

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval :
ExcludeArch: %{ix86}
# abc use broken on all Big Endian CPUs, specifically s390x (see BZ 1937362, 1937395):
ExcludeArch: s390x

%description
Yosys is a framework for Verilog RTL synthesis. It currently has
extensive Verilog-2005 support and provides a basic set of synthesis
algorithms for various application domains.


%package doc
Summary:        Documentation for Yosys synthesizer

%description doc
Documentation for Yosys synthesizer.


%package share
Summary:        Architecture-independent Yosys files
BuildArch:      noarch

%description share
Architecture-independent Yosys files.


%package devel
Summary:        Development files to build Yosys synthesizer plugins
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       tcl-devel

%description devel
Development files to build Yosys synthesizer plugins.


%prep
%setup -q -n %{name}-%{commit0}

%patch 1 -p1 -b .cfginc
%patch 2 -p1 -b .mancfginc

# Ensure that Makefile doesn't wget viz.js
cp %{SOURCE1} .

# Get man pages from Debian
%setup -q -T -D -a 2 -n %{name}-%{commit0}

# Remove '/usr/bin/env', without changing timestamps, in all python shebangs:
for f in `find . -name \*.py`
do
    sed 's|/usr/bin/env python3|/usr/bin/python3|' $f >$f.new
    touch -r $f $f.new
    mv $f.new $f
done

make config-gcc

# Change manual source files to use libertine font rather than non-free luximono
for f in `find manual -name \*.tex -exec grep -l {luximono} {} \;`
do
    sed -i 's|{luximono}|{libertine}|' $f
done


%build
# disable LTO to allow building for f33 rawhide (BZ 1865657):
%define _lto_cflags %{nil}
%set_build_flags
make %{?_smp_mflags} PREFIX="%{_prefix}" ABCEXTERNAL=%{_bindir}/abc PRETTY=0 all
#manual
touch manual/empty.pdf

%global man_date "`stat -c %y debian/man/yosys-smtbmc.txt | awk '{ print $1 }'`"
txt2man -d %{man_date} -t YOSYS-SMTBMC debian/man/yosys-smtbmc.txt >yosys-smtbmc.1


%install
%make_install PREFIX="%{_prefix}" ABCEXTERNAL=%{_bindir}/abc STRIP=/bin/true

# move include files to includedir
install -d -m0755 %{buildroot}%{_includedir}
mv %{buildroot}%{_datarootdir}/%{name}/include %{buildroot}%{_includedir}/%{name}

# install man mages
install -d -m0755 %{buildroot}%{_mandir}/man1
install -m 0644 yosys-smtbmc.1 debian/yosys{,-config,-filterlib}.1 %{buildroot}%{_mandir}/man1

# install documentation
install -d -m0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 manual/*.pdf %{buildroot}%{_docdir}/%{name}

%check
make test ABCEXTERNAL=%{_bindir}/abc SEED=314159265359


%files
# license texts requested upstream:
#   https://github.com/YosysHQ/yosys/issues/263
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-filterlib
%{_bindir}/%{name}-smtbmc
%{_bindir}/%{name}-witness
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-filterlib.1*
%{_mandir}/man1/%{name}-smtbmc.1*

%files share
%{_datarootdir}/%{name}

%files doc
%{_docdir}/%{name}

%files devel
%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_mandir}/man1/%{name}-config.1*


%changelog
* Wed Aug 09 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.32.1.20230809git389b8d0
- update to 0.32 snapshot
- switch abc [build]requires to yosyshq-abc

* Wed Aug 02 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.31.2.20230729gitb04d0e0
- drop i686 (https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval)

* Sat Jul 29 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.31.1.20230729gitb04d0e0
- update to 0.31 snapshot

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2.20230607git5813809
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 07 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.30.1.20230607git5813809
- update to 0.30 snapshot

* Thu May 11 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.29.1.20230511gitd82bae3
- update to 0.29 snapshot

* Sun Apr 23 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.28.1.20230423git51dd029
- update to 0.28 snapshot

* Tue Mar 07 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.27.1.20230307gitb58664d
- update to 0.27 snapshot

* Wed Feb 15 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.26.1.20230215git1c667fa
- update to 0.26 snapshot

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2.20230104git7bac192
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.25.1.20230104git7bac192
- update to 0.25 snapshot

* Fri Dec 09 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.24.1.20221209git7ad7b55
- update to 0.24 snapshot

* Wed Nov 09 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.23.1.20221109gitc75f12a
- update to 0.23 snapshot

* Thu Oct 06 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.22.1.20221006gitc4a52b1
- update to 0.22 snapshot

* Mon Sep 12 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.21.1.20220921gitd98738d
- update to 0.21 snapshot

* Sun Aug 21 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.20.1.20220821git029c278
- update to 0.20 snapshot

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2.20220705git086c2f3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.19.1.20220705git086c2f3
- update to 0.19 snapshot

* Sat Jun 11 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.18.1.20220611gitb15a46c
- update to 0.18 snapshot

* Mon May 09 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.17.1.20220509git587e09d
- update to 0.17 snapshot

* Thu Apr 07 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.16.1.20220407git4da3f28
- update to 0.16 snapshot

* Fri Mar 04 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.15.1.20220304gitc312402
- update to 0.15 snapshot

* Tue Feb 22 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.14.1.20220222gita41c1df
- update to 0.14 snapshot

* Thu Jan 27 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.13.2.20220127git0e97c3f
- update to newer 0.13 snapshot
- remove pdf manual patch (issue fixed upstream)

* Thu Jan 27 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.13.1.20220127git84f0df1
- update to 0.13 snapshot (#2039600, #2047137)
- patch to restore ability to build the .pdf manual (upstream PR #3156)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12- 3.20211209gitcdb5711
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 0.12-2.20211209gitcdb5711
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Dec 09 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.12.1.20211209gitcdb5711
- update to 0.12 snapshot (#2028824)

* Sat Nov 06 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.11.1.20211106git9a41380
- update snapshot

* Tue Sep 28 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.10.1.20210928git62739f7
- update snapshot

* Sun Sep 05 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.9.16.20210904git50be8fd
- undo 'single thread to avoid race condition while building pdf doc'

* Sun Sep 05 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.9.15.20210904git50be8fd
- use single thread to avoid race condition in pdf doc build

* Sat Sep 04 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.9.14.20210904git50be8fd
- update snapshot

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13.20210523gitdf2b79c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.9.12.20210523gitdf2b79c
- update snapshot

* Wed Mar 10 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.9-11.20210310git26e01a6
- exclude arch s390x (abc use broken on all Big Endian CPUs, see BZ 1937362, 1937395)

* Sun Mar 07 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.9-10.20210307git9cdc6b5
- Switch to snapshots (releases are too infrequent w.r.t. development speed)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Jeff Law <law@redhat.com> - 0.9-8
- Fix missing #include for gcc-11

* Thu Aug 06 2020 Gabriel Somlo <gsomlo@gmail.com> - 0.9-7
- Disable LTO for f33 rebuild (BZ 1865657)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 Dan Horák <dan[at]danny.cz> - 0.9-4
- updated Requires for yosys-devel

* Sun Apr 19 2020 Marcus A. Romer <aimylios@gmx.de> - 0.9-3
- Update man pages from Debian
- Add license text

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.9-1
- Update to latest release
- Spec file cleanup

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8-4
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Jon Burgess <jburgess777@gmail.com> - 0.8-2
- Add buildreq for g++

* Sat Oct 27 2018 Jon Burgess <jburgess777@gmail.com> - 0.8-1
- Updated to latest upstream release
- Make sure package built with Fedora compile flags
- Fix assert while running tests
- Fixes FTBFS #1606769

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.7-9
- rebuilt due new iverilog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7-3
- Rebuild for readline 7.x

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7-2
- Rebuild for Python 3.6

* Sat Nov 26 2016 Eric Smith <brouhaha@fedoraproject.org> 0.7-1
- Updated to latest upstream release.
- Additional changes per package review.

* Fri Nov 04 2016 Eric Smith <brouhaha@fedoraproject.org> 0.6.0-2.20160923git8f5bf6d
- Updated per Randy Barlow's package review comments of 2016-10-20.

* Sat Sep 24 2016 Eric Smith <brouhaha@fedoraproject.org> 0.6.0-1.20160923git8f5bf6d
- Initial version (#1375765).
