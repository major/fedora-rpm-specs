Name:           python-pygeoif
Version:        1.6.0
Release:        %autorelease
Summary:        A basic implementation of the __geo_interface__

License:        LGPL-2.1-or-later
URL:            https://github.com/cleder/pygeoif/
#Source:         %%{url}archive/%%{version}.tar.gz
# tar -xzf %%{version}.tar.gz ; rm -f pygeoif-%%{version} pygeoif-%%{version}/test/hypothesis/test_functions.py ; tar -czf %%{version}.tar.gz
Source:         %{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(typing-extensions)

%global _description %{expand:
PyGeoIf provides a GeoJSON-like protocol for geo-spatial (GIS) vector data.}

%description %_description

%package -n     python3-pygeoif
Summary:        %{summary}

%description -n python3-pygeoif %_description

%prep
%autosetup -p1 -n pygeoif-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
pushd docs
sphinx-build -b man . man
popd

%install
%pyproject_install
%pyproject_save_files -L pygeoif
mkdir -p %{buildroot}%{_mandir}/man1
install -m0644 docs/man/pygeoif.1 %{buildroot}%{_mandir}/man1/

%check
%pyproject_check_import
%pytest -k "not test_interiors and not test_from_wkt_epsg_4326 and not test_repr_eval and not test_convex_hull_bounds and not test_shape_2d and not test_shape_3d and not test_shape"

%files -n python3-pygeoif -f %{pyproject_files}
%license docs/LICENSE.GPL
%{_mandir}/man1/pygeoif.1*


%changelog
%autochangelog
