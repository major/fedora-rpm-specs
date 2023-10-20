Name:           python-gelidum
Version:        0.7.0
Release:        %autorelease
Summary:        Freeze your objects in python

# The entire source is MIT except resources/gelidum.jpg, which is CC0 (and is
# not installed)
License:        MIT
URL:            https://github.com/diegojromerolopez/gelidum
Source0:        %{url}/archive/v%{version}/gelidum-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Inspired by the method freeze found in other languages like
Javascript, this package tries to make immutable objects to make it
easier avoiding accidental modifications in your code.}

%description %_description

%package -n python3-gelidum
Summary:        %{summary}

%description -n python3-gelidum %_description


%prep
%autosetup -p1 -n gelidum-%{version}


%generate_buildrequires
# The build/test/runtime BuildRequires are generated from upstream metadata
%pyproject_buildrequires -r


%build
# The macro supports setup.py-based and pyproject.toml-based build
%pyproject_wheel


%install
# The macro supports setup.py-based and pyproject.toml-based build
%pyproject_install

# Library and metadata files can be saved automatically
%pyproject_save_files gelidum


%check
# %%tox
# for projects without tox, %%pytest is preferred
python3 -m unittest discover -s ./gelidum/tests


# %%{pyproject_files} handles code files, but executables,
# documentation and license must be listed in the spec file:
%files -n python3-gelidum -f %{pyproject_files}
%doc README.md
%license LICENSE
%exclude %{python3_sitelib}/gelidum/tests

%changelog
%autochangelog
