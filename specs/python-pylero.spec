Name:           python-pylero
Version:        0.1.0
Release:        4%{?dist}
Summary:        Python SDK for Polarion

License:        MIT
URL:            https://github.com/RedHatQE/pylero
Source:         %{url}/archive/%{version}/pylero-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is Pylero, the Python wrapper for the Polarion WSDL API. The Pylero
wrapper enables native python access to Polarion objects and functionality
using object oriented structure and functionality. This allows the devlopers to
use Pylero in a natural fashion without being concerned about the Polarion
details.

All Pylero objects inherit from BasePolarion. The objects used in the library
are all generated from the SOAP factory class, using the python-suds library.
The Pylero class attributes are generated dynamically as properties, based on
a mapping dict between the pylero naming convention and the Polarion attribute
names.

The use of properties allows the pylero object attributes to be virtual with no
need for syncing between them and the Polarion objects they are based on.

The Polarion WSDL API does not implement validation/verification of data passed
in, so the Pylero library takes care of this itself. All enums are validated
before being sent to the server and raise an error if not using a valid value.
A number of workflow implementations are also included, for example when
creating a Document, it automatically creates the Heading work item at the same
time.

Polarion Work Items are configured per installation, to give native workitem
objects (such as TestCase), the library connects to the Polarion server,
downloads the list of workitems and creates them.}

%description %_description

%package -n python3-pylero
Summary:        %{summary}

%description -n python3-pylero %_description


%prep
%autosetup -p1 -n pylero-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files pylero


%global _pylero_import_exclude %{expand:
-e pylero.build -e pylero.build_linked_work_item -e pylero.cli.cmd -e pylero.document
-e pylero.plan -e pylero.plan_record -e pylero.test_record -e pylero.test_run
-e pylero.work_item
}

%check
# If the Polarion server URL is not specified in config some libraries will
# fail to import, so exclude the modules which require the server url
%pyproject_check_import %_pylero_import_exclude


%files -n python3-pylero -f %{pyproject_files}
%doc README.md
%{_bindir}/pylero
%{_bindir}/pylero-cmd


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.13

* Tue May 21 2024 Wayne Sun <gsun@redhat.com> 0.1.0-1
- Update to 0.1.0

* Tue Mar 05 2024 Wayne Sun <gsun@redhat.com> 0.0.9-1
- Update to 0.0.9

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.0.8-2
- Rebuilt for Python 3.12

* Tue Mar 14 2023 Wayne Sun <gsun@redhat.com> 0.0.8-1
- Update to 0.0.8

* Thu Feb 23 2023 Wayne Sun <gsun@redhat.com> 0.0.7-1
- Update to 0.0.7

* Fri Feb 17 2023 Wayne Sun <gsun@redhat.com> 0.0.6-1
- Update to 0.0.6

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Wayne Sun <gsun@redhat.com> 0.0.5-1
- Update to 0.0.5

* Wed Dec 7 2022 Wayne Sun <gsun@redhat.com> 0.0.4-1
- Initial packaging
