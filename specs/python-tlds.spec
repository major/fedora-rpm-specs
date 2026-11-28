Name:           python-tlds
Version:        2026112100
Release:        %autorelease
Summary:        Automatically updated list of valid TLDs taken directly from IANA

License:        MIT
URL:            https://github.com/kichik/tlds
Source:         %{pypi_source tlds}

BuildSystem:    pyproject
BuildOption(install):  --assert-license tlds

BuildArch:      noarch


%global _description %{expand:
The tlds module provides a set of valid TLDs directly taken from IANA.
}

%description %_description

%package -n     python3-tlds
Summary:        %{summary}

%description -n python3-tlds %_description


%files -n python3-tlds -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
