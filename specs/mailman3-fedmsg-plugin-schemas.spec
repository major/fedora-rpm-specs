%global modname mailman3_fedmsg_plugin_schemas

%{!?python3_pkgversion: %global python3_pkgversion 3}

Name:               mailman3-fedmsg-plugin-schemas
Version:            1.0.0
Release:            4%{?dist}
Summary:            Fedora Messaging schema for messages emitted by Mailman 3

License:            LGPL-3.0-or-later
URL:                https://github.com/fedora-infra/mailman3-fedmsg-plugin
Source0:            %{pypi_source %modname}

BuildArch:          noarch

BuildRequires:      python%{python3_pkgversion}-devel

Requires:           fedora-messaging

%global _description %{expand:
  A schema describing fedora-messaging messages sent by mailman.
}

%description %_description

%package -n python3-%name
Summary: %{summary}

%description -n python3-%name %_description

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pyproject_check_import %{modname}

%files -n python3-%{name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.13

* Thu Apr 04 2024 Michal Konečný <mkonecny@redhat.com> - 1.0.0-1
- Initial mailman3-fedmsg-plugin-schemas spec.
