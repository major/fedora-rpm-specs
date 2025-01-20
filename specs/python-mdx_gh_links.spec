Name:           python-mdx_gh_links
Version:        0.4
Release:        6%{?dist}
Summary:        Python-Markdown Github-Links Extension

License:        BSD-3-Clause
URL:            https://github.com/Python-Markdown/github-links
Source0:        https://github.com/Python-Markdown/github-links/archive/%{version}/mdx_gh_links-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)


%description
This package provides an extension to Python-Markdown which adds support for
shorthand links to GitHub users, repositories, issues and commits.


%package -n python3-mdx_gh_links
Summary:        %{summary}

%description -n python3-mdx_gh_links
This package provides an extension to Python-Markdown which adds support for
shorthand links to GitHub users, repositories, issues and commits.


%generate_buildrequires
%pyproject_buildrequires -r


%prep
%autosetup -n github-links-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files mdx_gh_links


%check
%pytest


%files -n python3-mdx_gh_links -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Sandro Mani <manisandro@gmail.com> - 0.4-1
- Update to 0.4

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 0.3.1-1
- Update to 0.3.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Sandro Mani <manisandro@gmail.com> - 0.3-1
- Update to 0.3

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Sandro Mani <manisandro@gmail.com> - 0.2-8
- Modernize spec

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.2-3
- BR python3dist(setuptools)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2-2
- Rebuilt for Python 3.9

* Sun Mar  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.2-1
- Initial packaging
