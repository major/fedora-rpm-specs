%global framework kapidox

Name:    kf6-%{framework}
Version: 6.19.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 4 scripts and data for building API documentation

License: BSD
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

## downstream patches

# Fix kapidox installing in a broken state.
# See: https://invent.kde.org/frameworks/kapidox/-/issues/14
Patch0:  fix-broken-installation.patch

## upstream patches

# make sure BuildArch comes *after* patches, to ensure %%autosetup works right
BuildArch:      noarch

BuildRequires:  kf6-rpm-macros
BuildRequires:  python3-devel

Requires:       kf6-filesystem
Requires:       doxygen
Requires:       qt6-doc-devel

# Required for the import test
BuildRequires:  python3dist(gv)

%global __python %{__python3}
%global python_sitelib %{python3_sitelib}

%description
Scripts and data for building API documentation (dox) in a standard format and
style.


%prep
%autosetup -n %{framework}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files kapidox

%check
# Test suite don't run, so we'll do a simple import test.
%pyproject_check_import

%files -f %{pyproject_files}
%license LICENSES/*.txt
%{_kf6_bindir}/depdiagram_generate_all
%{_kf6_bindir}/kapidox-depdiagram-generate
%{_kf6_bindir}/kapidox-depdiagram-prepare
%{_kf6_bindir}/kapidox-generate


%changelog
* Sun Oct 05 2025 Steve Cossette <farchord@gmail.com> - 6.19.0-1
- 6.19.0

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 6.18.0-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Tue Sep 16 2025 farchord@gmail.com - 6.18.0-1
- 6.18.0

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 6.17.0-2
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Aug 01 2025 Steve Cossette <farchord@gmail.com> - 6.17.0-1
- 6.17.0

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jul 05 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.16.0-1
- 6.16.0

* Tue Jun 17 2025 Marie Loise Nolden <loise@kde.org> - 6.15.0-2
- 6.15 and plasma 3.4 compatibility rebuild

* Sat Jun 07 2025 Steve Cossette <farchord@gmail.com> - 6.15.0-1
- 6.15.0

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 6.14.0-2
- Rebuilt for Python 3.14

* Sat May 03 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.14.0-1
- 6.14.0

* Sun Apr 06 2025 Steve Cossette <farchord@gmail.com> - 6.13.0-1
- 6.13.0

* Fri Mar 07 2025 Steve Cossette <farchord@gmail.com> - 6.12.0-1
- 6.12.0

* Fri Feb 07 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.11.0-1
- 6.11.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 03 2025 Steve Cossette <farchord@gmail.com> - 6.10.0-1
- 6.10.0

* Sat Dec 14 2024 Steve Cossette <farchord@gmail.com> - 6.9.0-1
- 6.9.0

* Sat Nov 02 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.8.0-1
- 6.8.0

* Fri Oct 04 2024 Steve Cossette <farchord@gmail.com> - 6.7.0-1
- 6.7.0

* Mon Sep 16 2024 Steve Cossette <farchord@gmail.com> - 6.6.0-1
- 6.6.0

* Sat Aug 10 2024 Steve Cossette <farchord@gmail.com> - 6.5.0-1
- 6.5.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.0-1
- 6.4.0

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 6.3.0-2
- Rebuilt for Python 3.13

* Sat Jun 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Sat May 04 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Wed Apr 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.249.0-1
- 5.249.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Thu Jan 04 2024 Steve Cossette <farchord@gmail.com> - 5.247.0-2
- Added patch to fix broken installation

* Thu Jan 04 2024 Steve Cossette <farchord@gmail.com> - 5.247.0-1
- 5.247.0 for KF6 API
