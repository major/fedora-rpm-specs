%bcond tests 1

%global pypi_name pyunicorn

%global _description %{expand:
pyunicorn (Unified Complex Network and RecurreNce analysis toolbox)
is a fully object-oriented Python package for the advanced
analysis and modeling of complex networks. Above the standard measures
of complex network theory such as degree, betweenness and clustering 
coefficient it provides some uncommon but interesting statistics like 
Newman's random walk betweenness. pyunicorn features novel node-weighted
(node splitting invariant) network statistics as well as measures 
designed for analyzing networks of interacting/interdependent networks.}

Name:           python-%{pypi_name}
Version:        0.8.2
Release:        %{autorelease}
Summary:        Unified complex network and recurrence analysis toolbox

%global forgeurl https://github.com/pik-copan/pyunicorn
%global tag v%{version}
%forgemeta

License:        BSD-3-Clause
URL:            http://www.pik-potsdam.de/~donges/pyunicorn/
Source:         %{forgesource}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
# Listes as a test dependency, but also needed for import test
BuildRequires:  python3-matplotlib

# The tests extra also specifies linters. Therefore we specify manually.
%if %{with tests}
BuildRequires:  python3-cartopy
Buildrequires:  python3-networkx
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist
%endif

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
# Not specified upstream, but imported (from) in two places
Requires:       %{py3_dist matplotlib}
Obsoletes:      python-%{pypi_name}-doc < 0.8.0

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

for lib in $(find . -name "*.py"); do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%if %{with tests}
# Test requires network
k="${k-}${k+ and }not TestMapPlot"
%pytest ${k+-k "${k-}"}
%else
%pyproject_check_import
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
