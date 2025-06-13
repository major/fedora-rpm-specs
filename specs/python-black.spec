Name:           python-black
Version:        25.1.0
Release:        %autorelease
Summary:        The uncompromising code formatter
License:        MIT
URL:            https://github.com/psf/black
Source:         %{pypi_source black}

# Fix f-string format test failure with Python 3.14 and 3.13.4+
Patch:          https://github.com/psf/black/commit/5977532781.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# test requirements (upstream mixed with coverage, we hand-pick what we need only):
BuildRequires:  python3-pytest

# the black[jupyter] extra is allowed by default
# disable to avoid the ipython-black bootstrap loop
# note that tests/test_no_ipynb.py only runs without jupyter
# extra paranoid packagers can build this both with and without to run all tests
%bcond jupyter  1

# uvloop not ready for Python 3.14: https://bugzilla.redhat.com/2326210
%bcond uvloop   %[ 0%{?fedora} < 43 && 0%{?rhel} < 11 ]


%global _description %{expand:
Black is the uncompromising Python code formatter. By using it, you agree to
cease control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting.
You will save time and mental energy for more important matters.}

%description %_description


%package -n     black
Summary:        %{summary}
Recommends:     black+d = %{version}-%{release}
%py_provides    python3-black

# The [python2] extra was removed in 22.1.0
# This can be safely removed in Fedora 39+
Obsoletes:      black+python2 < 22.1.0

%if %{without uvloop}
# The [uvloop] extra was temporarily removed in 25.1.0
# This can be safely removed once it is back or in Fedora 45+
Obsoletes:      black+uvloop < 25.1.0
%endif

%description -n black %_description


%prep
%autosetup -n black-%{version} -p1


%generate_buildrequires
%global extras_without_d colorama%{?with_jupyter:,jupyter}%{?with_uvloop:,uvloop}
%pyproject_buildrequires -rx d,%{extras_without_d}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'black*' '_black*' blib2to3

for exe in black blackd; do
  ln -sr %{buildroot}%{_bindir}/${exe}{,-%{python3_version}}
done


%check
export PIP_INDEX_URL=http://host.invalid./
export PIP_NO_DEPS=yes
%pytest -Wdefault -rs --run-optional %{!?with_jupyter:no_}jupyter


%files -n black -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/black
%{_bindir}/black-%{python3_version}

%pyproject_extras_subpkg -n black d
%{_bindir}/blackd
%{_bindir}/blackd-%{python3_version}

%pyproject_extras_subpkg -n black %{extras_without_d}


%changelog
%autochangelog
