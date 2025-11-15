Name:           fmf-jinja
Version:        0.1.0
Release:        %autorelease
Summary:        Jinja template engine using FMF metadata

License:        GPL-3.0-or-later
URL:            https://github.com/LecrisUT/fmf-jinja
Source:         %{pypi_source fmf_jinja}

BuildArch:      noarch
BuildRequires:  python3-devel

%py_provides python3-fmf-jinja

%description
Jinja template engine using FMF metadata


%prep
%autosetup -n fmf_jinja-%{version}
# Workaround for hatchling not preserving symlinks
# https://github.com/pypa/hatch/issues/2008
mkdir -p test/data/input
cp -r example/* test/data/input


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fmf_jinja


%check
%pytest


%files -f %{pyproject_files}
%{_bindir}/fmf-jinja
%doc README.md


%changelog
%autochangelog
