%global short_name lsp-jsonrpc

%global _description %{expand:
A python server implementation of JSON RPC 2.0 protocol. This library
has been pulled out of the python LSP server project (a community maintained
fork of python-language-server).
}

Name:           python-%{short_name}
Version:        1.0.0
Release:        7%{?dist}
Summary:        Python implementation of JSON RPC 2.0 protocol

License:        MIT
URL:            https://github.com/python-lsp/python-lsp-jsonrpc
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}

%description -n python3-%{short_name} %_description


%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pylsp_jsonrpc

%check
%pytest

%files -n python3-%{short_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.0-2
- Use pytest macro
- address other spec sanity comments

* Mon Jul 05 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.0-1
- Initial package
