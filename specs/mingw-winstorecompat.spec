%?mingw_package_header

#%%global snapshot_date 20140912
#%%global snapshot_rev b08afbb5768898ae9c6d0d2798aaccf4f21de361
#%%global snapshot_rev_short %(echo %snapshot_rev | cut -c1-6)
#%%global branch trunk

# Run the testsuite
%global enable_tests 0

Name:           mingw-winstorecompat
Version:        4.0.2
Release:        21%{?dist}
Summary:        MinGW library to help porting to Windows Store
License:        MIT

URL:            http://mingw-w64.sourceforge.net/
%if 0%{?snapshot_date}
# To regenerate a snapshot:
# Use your regular webbrowser to open https://sourceforge.net/p/mingw-w64/mingw-w64/ci/%{snapshot_rev}/tarball
# This triggers the SourceForge instructure to generate a snapshot
# After that you can pull in the archive with:
# spectool -g mingw-winstorecompat.spec
Source0:        http://sourceforge.net/code-snapshots/git/m/mi/mingw-w64/mingw-w64.git/mingw-w64-mingw-w64-%{snapshot_rev}.zip
%else
Source0:        http://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}%{?pre:-%{pre}}.tar.bz2
%endif

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-headers >= 2.0.999-0.24.trunk.20130520
BuildRequires:  mingw64-headers >= 2.0.999-0.24.trunk.20130520


%description
This library can be linked to code targetting Windows Store.
Functions that are not available anymore for Windows Store are redefined,
using similar functions that are allowed.
'Forbidden' functions can be found either by browsing MSDN, either by
running WACK (Windows Application Certification Kit) on the application.

%package -n mingw32-winstorecompat
Summary:        MinGW library to help porting to Windows Store for the win32 target

%description -n mingw32-winstorecompat
This library can be linked to code targetting Windows Store.
Functions that are not available anymore for Windows Store are redefined,
using similar functions that are allowed.
'Forbidden' functions can be found either by browsing MSDN, either by
running WACK (Windows Application Certification Kit) on the application.

%package -n mingw64-winstorecompat
Summary:        MinGW library to help porting to Windows Store for the win64 target

%description -n mingw64-winstorecompat
This library can be linked to code targetting Windows Store.
Functions that are not available anymore for Windows Store are redefined,
using similar functions that are allowed.
'Forbidden' functions can be found either by browsing MSDN, either by
running WACK (Windows Application Certification Kit) on the application.


# The debuginfo subpackages are not needed for this package
# because winstorecompat is a static library and static
# libraries are stripped by default which cause debuginfo
# subpackages to remain empty


%prep
%if 0%{?snapshot_date}
rm -rf mingw-w64-v%{version}
mkdir mingw-w64-v%{version}
cd mingw-w64-v%{version}
unzip %{S:0}
%setup -q -D -T -n mingw-w64-v%{version}/mingw-w64-mingw-w64-%{snapshot_rev}
%else
%setup -q -n mingw-w64-v%{version}
%endif


%build
pushd mingw-w64-libraries/winstorecompat
    %mingw_configure
    %mingw_make %{?smp_mflags}
popd


%install
pushd mingw-w64-libraries/winstorecompat
    %mingw_make install DESTDIR=$RPM_BUILD_ROOT
popd

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n mingw32-winstorecompat
%doc COPYING
%{mingw32_libdir}/libwinstorecompat.a

%files -n mingw64-winstorecompat
%doc COPYING 
%{mingw64_libdir}/libwinstorecompat.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 4.0.2-15
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2

* Sun Mar 29 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1
- Removed empty debuginfo subpackages

* Fri Sep 12 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.9.999-0.1.trunk.git.b08afb.20140912
- Update to 20140912 snapshot (git rev b08afb)
- Bump version as upstream released mingw-w64 v3.2.0 recently (which is not based on the trunk branch)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.999-0.2.trunk.git502c72.20140524
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.999-0.1.trunk.git502c72.20140524
- Update to 20140524 snapshot (git rev 502c72)
- Upstream has switched from SVN to Git

* Fri Aug 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.4.trunk.r6069.20130810
- Update to r6069 (20130810 snapshot)
- Updated instructions to regenerate snapshots
  (SourceForge has changed their SVN infrastructure)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.999-0.3.trunk.20130520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.2.trunk.20130520
- Update to 20130520 snapshot
- Bumped BR: mingw32-headers mingw64-headers to >= 2.0.999-0.24.trunk.20130520 because of combaseapi.h

* Thu May  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.1.trunk.20130509
- Initial package

