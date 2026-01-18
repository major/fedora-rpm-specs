%global commit 3a7c84896f2dcdbd6fc13fb5df11af43b92ec850
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20240927

Name:           almalinux-git-utils
Version:        0.0.3^git%{commitdate}.%{shortcommit}
Release:        7%{?dist}
Summary:        Utilities for working with the AlmaLinux Git server

License:        GPL-3.0-or-later
URL:            https://git.almalinux.org/almalinux/almalinux-git-utils
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)


%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l almalinux


%check
%pytest -v


%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/alma_blob_upload
%{_bindir}/alma_get_sources


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3^git20240927.3a7c848-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3^git20240927.3a7c848-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.0.3^git20240927.3a7c848-5
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.0.3^git20240927.3a7c848-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3^git20240927.3a7c848-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jun 06 2025 Python Maint <python-maint@redhat.com> - 0.0.3^git20240927.3a7c848-2
- Rebuilt for Python 3.14

* Fri May 30 2025 Neal Gompa <ngompa@almalinux.org> - 0.0.3^git20240927.3a7c848-1
- Initial package
