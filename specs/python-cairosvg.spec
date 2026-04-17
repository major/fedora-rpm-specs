%global modname cairosvg
%global srcname cairosvg
%global py3_prefix python%{python3_pkgversion}

Name:               python-cairosvg
Version:            2.9.0
Release:            %autorelease
Summary:            A Simple SVG Converter for Cairo

License:            LGPL-3.0-or-later
URL:                https://cairosvg.org/
Source0:            %pypi_source
Patch0:             %{name}-disable-flake8-isort.patch

BuildArch:          noarch

BuildRequires:      %{py3_prefix}-devel


%description
CairoSVG is a SVG 1.1 to PNG, PDF, PS and SVG converter which can also be used
as a Python library.

%package -n python3-cairosvg
Summary:            A Simple SVG Converter for Cairo

# The subpackage used to be called this on accident.
# https://bugzilla.redhat.com/show_bug.cgi?id=1263793
Provides:           python3-CairoSVG

# %%{_bindir}/cairosvg was moved from here
Conflicts:          python2-cairosvg < 1.0.20-11


%description -n python3-cairosvg
CairoSVG is a SVG converter based on Cairo. It can export SVG files to PDF,
PostScript and PNG files.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cairosvg

%check
%pytest -v


%files -n python3-cairosvg -f %{pyproject_files}
%doc README.rst
%{_bindir}/cairosvg

%changelog
%autochangelog
