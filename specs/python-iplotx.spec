# NOTE: We do not build documentation due to missing dependencies:
# - cogent3
# - dendropy

%global giturl  https://github.com/fabilab/iplotx

Name:           python-iplotx
Version:        1.7.0
Release:        %autorelease
Summary:        Visualize networks and trees

License:        MIT
URL:            https://iplotx.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/iplotx-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -L iplotx

# Tests
BuildRequires:  %{py3_dist biopython}
BuildRequires:  %{py3_dist igraph}
BuildRequires:  %{py3_dist mypy}
BuildRequires:  %{py3_dist networkx}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist types-requests}

%global _desc %{expand:Visualize networks and trees in Python, with style.  Supports:

- networks
    - networkx
    - igraph
    - graph-tool
    - zero-dependency
- trees:
    - ETE4
    - cogent3
    - Biopython
    - scikit-bio
    - dendropy
    - zero-dependency

In addition to the above, any network or tree analysis library can register an
entry point to gain compatibility with iplotx with no intervention from our
side.}

%description
%_desc

%package -n python3-iplotx
Summary:        Visualize networks and trees

%description -n python3-iplotx
%_desc

%pyproject_extras_subpkg -n python3-iplotx igraph,networkx

%prep
%autosetup -p1 -n iplotx-%{version}

%check
# Some tests are sensitive to the version of matplotlib.  Skip those tests to
# avoid spurious failures.
k="${k-}${k+ and }not (test_complex)"
k="${k-}${k+ and }not (test_curved_waypoints)"
k="${k-}${k+ and }not (test_directed_graph)"
k="${k-}${k+ and }not (test_display_shortest_path)"
k="${k-}${k+ and }not (test_leaf_labels)"
k="${k-}${k+ and }not (test_labels)"
k="${k-}${k+ and }not (test_leafedges)"
k="${k-}${k+ and }not (test_show_support)"
k="${k-}${k+ and }not (test_vertex_labels)"
%pytest -v -k "${k-}"

%files -n python3-iplotx -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
