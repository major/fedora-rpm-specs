Name:           python-nitrokey
Version:        0.4.2
Release:        %autorelease
Summary:        Nitrokey Python SDK

License:        Apache-2.0 OR MIT
URL:            https://github.com/Nitrokey/nitrokey-sdk-py
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

%if 0%{fedora} <= 45
# Rebased version of https://github.com/Nitrokey/nitrokey-sdk-py/blob/2221ef1fa9dc30ab50f538446d6262e23a19a0be/ci-scripts/linux/rpm/protobuf.patch
# No longer required since https://fedoraproject.org/wiki/Changes/Protobuf_5.x/6.x
Patch:          protobuf.patch
%endif

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
%{summary}.}

%description %_description

%package -n     python3-nitrokey
Summary:        %{summary}

%description -n python3-nitrokey %_description


%prep
%autosetup -p1 -n nitrokey-sdk-py-%{version}

%pyproject_patch_dependency hidapi:drop_upper


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l nitrokey -L


%check
%{py3_test_envvars} %{python3} -m unittest


%files -n python3-nitrokey -f %{pyproject_files}
%license LICENSES/*
%doc README.md

%changelog
%autochangelog
