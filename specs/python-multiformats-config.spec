Name:           python-multiformats-config
Version:        0.3.1
Release:        %autorelease
Summary:        Pre-loading configuration module for the _multiformats_ package

# multiformats_config/__init__.py is LGPL-2.1-or-later
# ADDITIONAL_LICENSES mention use of PublicDomain, but it is not present in tarball
License:        MIT AND LGPL-2.1-or-later
URL:            https://github.com/hashberg-io/multiformats-config
Source:         %{pypi_source multiformats-config}

BuildSystem:    pyproject
BuildOption(install):  --assert-license multiformats_config
BuildOption(generate_buildrequires): -x dev

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Pre-loading configuration module for the _multiformats_ package.
}

%description %_description

%package -n     python3-multiformats-config
Summary:        %{summary}

%description -n python3-multiformats-config %_description

%pyproject_extras_subpkg -n python3-multiformats-config dev

%prep -a
# to break circular deps and it is needed only for install
%pyproject_patch_dependency multiformats:ignore

%files -n python3-multiformats-config -f %{pyproject_files}


%changelog
%autochangelog
