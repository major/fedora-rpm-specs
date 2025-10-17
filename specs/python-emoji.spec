%global pypi_name emoji

Name:           python-%{pypi_name}
Version:        2.15.0
Release:        %autorelease
Summary:        Emoji library for Python

%global forgeurl https://github.com/carpedm20/emoji
%global tag v%{version}
%forgemeta

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Full featured simple emoji library for Python. This project was
inspired by kyokomi.

The entire set of Emoji codes as defined by the unicode consortium is
supported in addition to a bunch of aliases. By default, only the
official list is enabled but doing emoji.emojize(use_aliases=True)
enables both the full list and aliases.}

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -r fEs

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CHANGES.md

%changelog
%autochangelog
