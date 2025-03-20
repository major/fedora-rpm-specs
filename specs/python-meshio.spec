%global pypi_name meshio

# The base package is arched, since we need the ParaView plugin to be
# arched, so it is installed into the correct %%_libdir.
%global debug_package %{nil}

Name:           python-%{pypi_name}
Version:        5.3.5
Release:        %{autorelease}
Summary:        I/O for many mesh formats

%global forgeurl https://github.com/nschloe/meshio
%forgemeta

License:        MIT
URL:            %forgeurl
Source0:        %forgesource
# See README-test-files.md in dist-git for an explanation and instructions
Source1:        %{pypi_name}-test-files-5.3.5.tar.gz

# Do not rely on repr() of np.float64
# https://github.com/nschloe/meshio/pull/1506
#
# Partial fix for:
#
# [BUG] Tests fail with NumPy 2.2.0
# https://github.com/nschloe/meshio/issues/1499
Patch:          %{forgeurl}/pull/1513.patch

ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  help2man

%global _description %{expand:
There are various mesh formats available for representing unstructured
meshes. meshio can read and write all of the following and smoothly
converts between them:

  Abaqus (.inp), ANSYS msh (.msh), AVS-UCD (.avs), CGNS (.cgns),
  DOLFIN XML (.xml), Exodus (.e, .exo), FLAC3D (.f3grid), H5M (.h5m),
  Kratos/MDPA (.mdpa), Medit (.mesh, .meshb), MED/Salome (.med),
  Nastran (bulk data, .bdf, .fem, .nas), Netgen (.vol, .vol.gz),
  Neuroglancer precomputed format,
  Gmsh (format versions 2.2, 4.0, and 4.1, .msh), OBJ(.obj), OFF (.off),
  PERMAS (.post, .post.gz, .dato, .dato.gz),
  PLY (.ply), STL (.stl), Tecplot .dat, TetGen .node/.ele,
  SVG (2D output only) (.svg), SU2 (.su2), UGRID (.ugrid),
  VTK (.vtk), VTU (.vtu), WKT (TIN) (.wkt), XDMF (.xdmf, .xmf).}

%description %_description


%package -n python3-%{pypi_name}
BuildArch:      noarch
Summary:        %{summary}
Recommends:     (paraview-%{pypi_name} if paraview)

%description -n python3-%{pypi_name} %_description


%package -n paraview-%{pypi_name}
Summary:        ParaView plugin for %{pypi_name}
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       paraview

%description -n paraview-%{pypi_name}
Package provides a ParaView plugin for viewing all meshio supported files.


%pyproject_extras_subpkg -a -n python3-%{pypi_name} all


%prep
%forgeautosetup -p1

# Install test files
tar xzvf %{SOURCE1}


%generate_buildrequires
%pyproject_buildrequires -x all


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

# Create and install man pages
mkdir -p %{buildroot}%{_mandir}/man1
%{py3_test_envvars} \
  help2man --no-info --version-string '%{pypi_name} %{version}' \
  -o %{buildroot}%{_mandir}/man1/%{pypi_name}.1 --no-discard-stderr \
  %{buildroot}%{_bindir}/%{pypi_name}
# sub commands
for SUBCMD in convert info compress decompress ascii binary; do \
  %{py3_test_envvars} \
    help2man --no-info --version-string '%{pypi_name} %{version}' \
    -o %{buildroot}%{_mandir}/man1/%{pypi_name}-${SUBCMD}.1 --no-discard-stderr \
    %{buildroot}%{_bindir}/%{pypi_name}\ ${SUBCMD}; \
done

# Install ParaView plugin
for plugindir in \
  '%{buildroot}%{_libdir}/paraview/paraview/plugins' \
  '%{buildroot}%{_libdir}/mpich/lib/paraview/paraview/plugins' \
  '%{buildroot}%{_libdir}/openmpi/lib/paraview/paraview/plugins'
do
  install -t "${plugindir}/%{pypi_name}" -D -m 0644 -p 'tools/paraview-meshio-plugin.py'
  %py_byte_compile %{python3} "${plugindir}/%{pypi_name}"
done


%check
%pytest -r fEs


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md CITATION.cff
%{_bindir}/%{pypi_name}
%{_mandir}/man1/%{pypi_name}*


%files -n paraview-%{pypi_name}
# paraview: co-own plugin directory and necessary parents
%dir %{_libdir}/paraview
%dir %{_libdir}/paraview/paraview
%dir %{_libdir}/paraview/paraview/plugins
%dir %{_libdir}/paraview/paraview/plugins/%{pypi_name}
%dir %{_libdir}/paraview/paraview/plugins/%{pypi_name}/__pycache__
%pycached %{_libdir}/paraview/paraview/plugins/%{pypi_name}/paraview-meshio-plugin.py

# paraview-mpich: co-own plugin directory and necessary parents
%dir %{_libdir}/mpich
%dir %{_libdir}/mpich/lib
%dir %{_libdir}/mpich/lib/paraview
%dir %{_libdir}/mpich/lib/paraview/paraview
%dir %{_libdir}/mpich/lib/paraview/paraview/plugins
%dir %{_libdir}/mpich/lib/paraview/paraview/plugins/%{pypi_name}
%dir %{_libdir}/mpich/lib/paraview/paraview/plugins/%{pypi_name}/__pycache__
%pycached %{_libdir}/mpich/lib/paraview/paraview/plugins/%{pypi_name}/paraview-meshio-plugin.py

# paraview-openmpi: co-own plugin directory and necessary parents
%dir %{_libdir}/openmpi
%dir %{_libdir}/openmpi/lib
%dir %{_libdir}/openmpi/lib/paraview
%dir %{_libdir}/openmpi/lib/paraview/paraview
%dir %{_libdir}/openmpi/lib/paraview/paraview/plugins
%dir %{_libdir}/openmpi/lib/paraview/paraview/plugins/%{pypi_name}
%dir %{_libdir}/openmpi/lib/paraview/paraview/plugins/%{pypi_name}/__pycache__
%pycached %{_libdir}/openmpi/lib/paraview/paraview/plugins/%{pypi_name}/paraview-meshio-plugin.py


%changelog
%autochangelog
