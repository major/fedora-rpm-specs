%global pypi_name git_up

Name:           git-up
Version:        2.2.0
Release:        1%{?dist}
Summary:        A more friendly "git pull" in Python

License:        MIT
URL:            https://github.com/msiemens/PyGitUp
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/msiemens/PyGitUp/v%{version}/LICENCE
BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)

%description
PyGitUp is a Python port of aanand/git-up. It not only fully covers the
abilities of git-up and should be a drop-in replacement, but also extends it
slightly.

%prep
%autosetup -n %{pypi_name}-%{version}
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
