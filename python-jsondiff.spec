%global         srcname     jsondiff
%global         forgeurl    https://github.com/xlwings/jsondiff
Version:        2.0.0
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Diff JSON and JSON-like structures in Python

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Diff JSON and JSON-like structures in Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jsondiff

# Remove the jsondiff binary to avoid conflict with python-jsonpatch.
# See BZ 1967775 for more details.
rm -f %{buildroot}%{_bindir}/%{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/jdiff


%changelog
%autochangelog
