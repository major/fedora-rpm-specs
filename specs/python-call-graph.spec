Name:           python-call-graph
Version:        2.1.6
Release:        %autorelease
Summary:        Visualises the flow of your Python application 

License:        GPL-2.0-only
URL:            https://github.com/lewiscowles1986/py-call-graph/
Source:         %{pypi_source python-call-graph}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
This is a fork of the original, updated to work with Python 3.5 - 3.11 \
and from 2.1.4 3.8 - 3.13 \
See https://lewiscowles1986.github.io/py-call-graph/ for more information.}

%description %_description

%package -n     python3-python-call-graph
Summary:        %{summary}

%description -n python3-python-call-graph %_description

%pyproject_extras_subpkg -n python3-python-call-graph ipython,memory-psutil


%prep
%autosetup -p1 -n python-call-graph-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x ipython,memory-psutil


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pycallgraph

mkdir -p %{buildroot}%{_mandir}/man1/
cp -pr man/pycallgraph.1 %{buildroot}%{_mandir}/man1/

%check
%pyproject_check_import
# tests require calls module, which is not in Fedora and appears dormant upstream

%files -n python3-python-call-graph -f %{pyproject_files}
%{_bindir}/pycallgraph
%{_mandir}/man1/pycallgraph.1*

%changelog
%autochangelog
