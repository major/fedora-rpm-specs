Name:           verilator
Version:        4.226
Release:        1%{?dist}
Summary:        A fast simulator for synthesizable Verilog
License:        LGPLv3 or Artistic 2.0
URL:            https://veripool.org/verilator/
Source0:        https://github.com/verilator/verilator/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-lib
BuildRequires:  perl-version
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  python3-devel
BuildRequires:  sed

%description
Verilator is the fastest free Verilog HDL simulator. It compiles
synthesizable Verilog, plus some PSL, SystemVerilog and Synthesis
assertions into C++ or SystemC code. It is designed for large projects
where fast simulation performance is of primary concern, and is
especially well suited to create executable models of CPUs for
embedded software design teams.

%prep
%autosetup
find . -name .gitignore -delete
export VERILATOR_ROOT=%{_datadir}
autoconf
%{configure} \
    --disable-ccwarn \
    --enable-defenv \
    --disable-longtests

# We cannot run autoreconf because upstream uses unqualifed stdlib identifiers
# that are included by autoconf-generated header files.
find -name Makefile_obj -exec sed -i \
    -e 's|^\(COPT = .*\)|\1 %{optflags}|' \
    -e 's|^#LDFLAGS += .*|LDFLAGS += %{__global_ldflags}|' \
    {} \;

%build
%make_build

%check
make test

%install
%make_install

# remove the copy of examples in the datadir so we could
# mark the copy in the source directory as "doc"
rm -rf %{buildroot}%{_datadir}/verilator/examples

# remove not needed build directory and bin directory
rm -rf %{buildroot}%{_datadir}/verilator/src
rm -rf %{buildroot}%{_bindir}/verilator_includer

# verilator installs verilator.pc under ${datadir}
# but for consistency we want it under ${libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_datadir}/pkgconfig/verilator.pc %{buildroot}%{_libdir}/pkgconfig


%files
%license Artistic LICENSE
%doc Changes README*
%doc docs/
%doc examples/
%{_mandir}/man1/*.1.gz
%{_datadir}/verilator
%{_libdir}/pkgconfig/verilator.pc
%{_bindir}/verilator
%{_bindir}/verilator_bin
%{_bindir}/verilator_bin_dbg
%{_bindir}/verilator_coverage
%{_bindir}/verilator_coverage_bin_dbg
%{_bindir}/verilator_gantt
%{_bindir}/verilator_profcfunc


%changelog
* Sat Sep 24 2022 Filipe Rosset <rosset.filipe@gmail.com> - 4.226-1
- Update to 4.226, enabled tests, spec cleanup and modernization
- Fixes rhbz#1933296 rhbz#2047099 and rhbz#2026957

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.108-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.108-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.108-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Filipe Rosset <rosset.filipe@gmail.com> - 4.108-1
- Update to 4.108 fixes rhbz#1901487

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 24 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.032-1
- Update to 4.032

* Sun Feb 16 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.028-1
- Update to 4.028

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Filipe Rosset <rosset.filipe@gmail.com> - 4.026-1
- Update to 4.026 fixes rhbz#1747211

* Thu Aug 22 2019 Filipe Rosset <rosset.filipe@gmail.com> - 4.016-1
- Updated to 4.016 fixes rhbz#1590822 rhbz#1643479 and rhbz#1700228

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.922-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Scott Tsai scottt.tw@gmail.com - 3.922-5
- Remove duplicate copies of 'examples' in /usr/share/doc
- https://bugzilla.redhat.com/show_bug.cgi?id=1592057#c3

* Fri May 03 2019 Marcus Müller <marcus@hostalia.de> - 3.922-4
- Made %{_bindir}/verilator et al executable, fixes rhbz #1592057

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.922-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.922-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.922-1
- 3.922 bump, fixes rhbz #1557720

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.920-2
- Escape macros in %%changelog

* Wed Feb 07 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.920-1
- 3.920 bump
- Disabled tests until upstream fixes the issue
- Added BR to fix EPEL7 build
- Fixes rhbz #1250122 and rhbz #1494887

* Fri Sep 08 2017 Petr Pisar <ppisar@redhat.com> - 3.910-1
- 3.910 bump
- License corrected to (LGPLv3 or Artistic 2.0)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.890-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.890-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.890-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.890-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Filipe Rosset <rosset.filipe@gmail.com> - 3.890-2
- Attempt to rebuilt on rawhide due dependency problems

* Mon Nov 28 2016 Filipe Rosset <rosset.filipe@gmail.com> - 3.890-1
- Rebuilt for new upstream version 3.890
- Spec clean up plus fixes rhbz #1087393 and rhbz #1358609

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.874-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.874-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Scott Tsai <scottt.tw@gmail.com> - 3.874-1
- Upstream 3.874

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.864-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Sep 22 2014 Scott Tsai <scottt.tw@gmail.com> 3.864-1
- Upstream 3.864

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.862-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Scott Tsai <scottt.tw@gmail.com> 3.862-1
- Upstream 3.862

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.845-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.845-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 16 2013  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.845-1
- updated to 3.845

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.805-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.805-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.805-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.805-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.805-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 07 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.805-1
- updated to 3.805

* Sat Sep 25 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.804-1
- updated to 3.804

* Sun Jul 11 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.803-1
- updated to 3.803

* Fri Jul 24 2009 Lane Brooks <dirjud [AT] gmail DOT com> - 3.712-1
- Updated to verilator 3.712

* Fri Jun 26 2009 Lane Brooks <dirjud [AT] gmail DOT com> - 3.711-1
- Updated to verilator 3.711
- Added Artistic file
- Fixed permissions on man file

* Tue Jun 9 2009 Lane Brooks <dirjud [AT] gmail DOT com> - 3.710-1
- Updated to verilator 3.710
- Removed GCC 4.3 patch (no longer necessary)
- Added SYSTEMPERL_INCLUDE to point to perl-SystemPerl rpm install location

* Fri Jan 9 2009 Lane Brooks <dirjud [AT] gmail DOT com> - 3.700-1
- Updated dependancy to newly packaged perl-SystemPerl and removed patch
- Updated to verilator 3.700
- Added GCC 4.3 patch

* Fri Jan 2 2009 Lane Brooks <dirjud [AT] gmail DOT com> - 3.681-2
- Moved examples from data dir to doc dir

* Thu Jan 1 2009 Lane Brooks <dirjud [AT] gmail DOT com> - 3.681-1
- Updated verilator 3.681
- Removed gcc 4.3 patch as verilator 3.681 incorporates this fix
- Removed shared object patch as it is possible to do this from Makefile
  using environment variables
- Further updates to the spec file per Chitlesh's feedback

* Sun Oct 26 2008 Lane Brooks <dirjud [AT] gmail DOT com> - 3.680-3
- Improved spec file for Fedora integration based on initial feedback

* Thu Oct 23 2008 Lane Brooks <dirjud [AT] gmail DOT com> - 3.680-2
- Added shared object generation patch

* Thu Oct 16 2008 Lane Brooks <dirjud [AT] gmail DOT com> - 3.680-1
- Initial package based on SUSE packages from Guenter Dannoritzer <dannoritzer{%%}web{*}de>
