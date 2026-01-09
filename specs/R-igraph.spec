Name:           R-igraph
Version:        %R_rpm_version 2.2.1
Release:        %autorelease
Summary:        Network Analysis and Visualization

License:        GPL-2.0-or-later AND TCL
URL:            %{cran_url}
Source:         %{cran_source}
# Unbundle some things:
Patch:          0002-Unbundle-uuid.patch
# Patch:          0003-Unbundle-arpack.patch
# couldn't unbundle: undefined symbol: igraphdsaupd_

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  arpack-devel
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel

# https://github.com/igraph/rigraph/issues/268
# Not a released version.
Provides:       bundled(igraph) = 0.10.17
Provides:       bundled(arpack)

%description
Routines for simple graphs and network analysis. It can handle large graphs
very well and provides functions for generating random and regular graphs,
graph visualization, centrality methods and much more.

%prep
%autosetup -c -p1

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
