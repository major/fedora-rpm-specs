%global pypi_name git_up

Name:           git-up
Version:        2.2.0
Release:        10%{?dist}
Summary:        A more friendly "git pull" in Python

License:        MIT
URL:            https://github.com/msiemens/PyGitUp
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/msiemens/PyGitUp/v%{version}/LICENCE

# pytest 8 compatibility
# https://github.com/msiemens/PyGitUp/pull/135
Patch:          135.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
PyGitUp is a Python port of aanand/git-up. It not only fully covers the
abilities of git-up and should be a drop-in replacement, but also extends it
slightly.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files PyGitUp

%check
if ! git config user.name ; then
  git config --global user.name "user"
fi
if ! git config user.email ; then
  git config --global user.email "user@example.com"
fi
%pytest

%files -f %{pyproject_files}
%license LICENCE
%doc README.rst
%{_bindir}/git-up
%exclude %{python3_sitelib}/PyGitUp/tests

%changelog
* Fri Jan 31 2025 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-10
- Fix build with pytest 8
- Fixes: rhbz#2272982

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 23 2024 Tomáš Hrnčiar <thrnciar@redhat.com> - 2.2.0-8
- BuildRequire pytest < 8

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.0-6
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.0-2
- Rebuilt for Python 3.12

* Wed Jul 05 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.0-1
- Update to 2.2.0 which fixes rhbz#2211331

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Oct 13 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.1.0-1
- Update to 2.1.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Martin Jackson <mhjacks@swbell.net> - 2.0.1-2
- Add explicit dep on setuptools.

* Sat Aug 29 2020 Martin Jackson <mhjacks@swbell.net> - 2.0.1-1
- New upstream release.  Relaxes dep on colorama.

* Sun Aug 23 2020 Martin Jackson <mhjacks@swbell.net> - 1.6.1-6
- Comment out %check for now.  Change in git broke them.  Will be fixed in upstream 2.0.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Martin Jackson <mhjacks@swbell.net> - 1.6.1-1
- Initial release
