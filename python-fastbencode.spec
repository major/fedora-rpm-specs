%global pypi_name fastbencode

Name:           python-%{pypi_name}
Version:        0.0.9
Release:        5%{?dist}
Summary:        Implementation of bencode with optional fast C extensions

License:        GPLv2+ and MIT
#fastbencode is licensed under GPLv2+
#_bencode_py.py is licensed under MIT
URL:            https://github.com/breezy-team/fastbencode
Source:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.29
BuildRequires:  python3dist(setuptools)
BuildRequires:  gcc

%global _description %{expand:
fastbencode is an implementation of the bencode serialization format 
originally used by BitTorrent.
The package includes both a pure-Python version and an optional C extension 
based on Cython.
Both provide the same functionality, but the C extension provides 
significantly better performance.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{pypi_name}
%license COPYING
%doc README.md
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.9-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.9-2
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Ondřej Pohořelský <opohorel@redhat.com> - 0.0.9-1
- Initial package.
