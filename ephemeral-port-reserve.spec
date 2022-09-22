Name:           ephemeral-port-reserve
Version:        1.1.4
Release:        3%{?dist}
Summary:        Bind to an ephemeral port, force it into the TIME_WAIT state, and unbind it.

License:        MIT
URL:            https://github.com/Yelp/%{name}/
Source0:        https://github.com/Yelp/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Provide the python3-* namespace as the package
# can also be used as a library.
%py_provides python3-ephemeral-port-reserve

%global _description %{expand:
Bind to an ephemeral port, force it into the TIME_WAIT state, and unbind it.}


%description %_description

%prep
%autosetup -p1 -n ephemeral-port-reserve-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ephemeral_port_reserve


%check
%pyproject_check_import
%pytest


%files -f %{pyproject_files}
%{_bindir}/ephemeral-port-reserve
%doc README.md


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.4-2
- Rebuilt for Python 3.11

* Mon May 02 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.1.4-1
- Initial package