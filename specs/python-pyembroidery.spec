%global         srcname         pyembroidery
%global         forgeurl        https://github.com/EmbroidePy/pyembroidery
Version:        1.5.1
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Release:        2%{?dist}
Summary:        Library for reading and writing a variety of embroidery formats

License:        MIT
URL:            %{forgeurl}
# Use source from GitHub to get license files
Source:         %{forgesource}


BuildRequires:  python3-devel

BuildArch: noarch

%global _description %{expand:
pyembroidery was coded from the ground up with all projects in mind. It
includes a lot of higher level and middle level pattern composition
abilities, and should accounts for any knowable error. If you know an error
it does not account for, raise an issue. It should be highly robust with
a simple api so as to be reasonable for any python embroidery project.

It should be complex enough to go very easily from points to stitches, fine
grained enough to let you control everything, and good enough that you
shouldn't want to.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires


%build
# Fix incorrect line endings
sed -i 's/\r$//' README.md
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%python3 -m unittest discover test

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitelib}/test
 
%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 20 2024 Benson Muite <benson_muite@emailplus.org> - 1.5.1-1
- Upgrade to 1.5.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.36-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 1.4.36-2
- Rebuilt for Python 3.12

* Fri Jun 16 2023 Benson Muite <benson_muite@emailplus.org> - 1.4.36-1
- Initial packaging
