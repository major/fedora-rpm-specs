%if 0%{?fedora} >= 41
%bcond_without dnf5
%else
%bcond_with dnf5
%endif

%global __python %__python3

%global _desc \
DNF plugin to compare files from the original package contents with locally \
available files and display differences in text files, such as configuration \
changes or source code (for interpreted languages).

%global _summary Display local changes in files from installed RPM packages

Name:           dnf-plugin-diff
Version:        2.0
Release:        1%{?dist}
Summary:        %_summary

License:        GPL-2.0-or-later
URL:            https://github.com/praiskup/%name
Source0:        https://github.com/praiskup/%name/releases/download/v%version/%name-%version.tar.gz

BuildRequires:  python3-devel
BuildRequires:  /usr/bin/c++
BuildRequires:  make

Requires:       cpio
Requires:       python3-dnf
Requires:       python3-dnf-plugins-core
Requires:       file

Provides:       dnf-command(diff) = %version

%if %{with dnf5}
BuildRequires:  boost-devel
BuildRequires:  dnf5-devel
BuildRequires:  libdnf5-cli-devel
%else
BuildArch:      noarch
%endif

%description
%_desc


%if %{with dnf5}
%package -n dnf5-plugin-diff
Requires:       dnf5
Summary:        %_summary
Provides:       dnf5-command(diff) = %version

%description -n dnf5-plugin-diff
%_desc
%endif

%prep
%setup -q


%build
%if %{with dnf5}
%configure PYTHON=python3
%else
%configure PYTHON=python3 --disable-dnf5
%endif
%make_build


%install
%make_install


%files
%license COPYING
%doc README
%_libexecdir/dnf-diff-*
%python3_sitelib/dnf-plugins


%if %{with dnf5}
%files -n dnf5-plugin-diff
%license COPYING
%doc README
%_libexecdir/dnf-diff-*
%_libdir/dnf5/plugins/diff.so
%endif


%changelog
* Sun Feb 09 2025 Pavel Raiskup <praiskup@redhat.com> - 2.0-1
- new upstream release, with DNF5 support
  https://github.com/praiskup/dnf-plugin-diff/releases/tag/v2.0

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1-20
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 19 2023 Pavel Raiskup <praiskup@redhat.com> - 1.1-15
- fix FTI rhbz#2219976

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1-14
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1-11
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-8
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-5
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Pavel Raiskup <praiskup@redhat.com> - 1.1-1
- new release, fix for situation when package is provided by multiple
  repositories

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Pavel Raiskup <praiskup@redhat.com> - 1.0-2
- fix review issues spotted by Robert-André Mauchin

* Sat Dec 15 2018 Pavel Raiskup <praiskup@redhat.com> - 1.0-1
- initial Fedora packaging
