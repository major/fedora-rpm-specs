Name:           python-pyct
Version:        0.4.8
Release:        %autorelease
Summary:        Python packaging Common Tasks

# The entire source is BSD-3-Clause, except for pyct/cmd.py, which is
# (BSD-3-Clause and ISC).
License:        BSD-3-Clause AND ISC
URL:            https://github.com/pyviz-dev/pyct
# The PyPI archive lacks tox.ini, but it was not exactly suitable for testing
# in the RPM build environment anyway, so we just re-created the needed tests
# in %%check.
#
# Note that if we ever switch to the GitHub tarball we will need to re-create
# the pyct/.version file that appears in the PyPI source tarball in order for
# package versioning to work correctly. See the python-param package for an
# example of this.
Source0:        %{pypi_source pyct}

# Man pages written by hand for Fedora in groff_man(7) format using the
# command’s --help output
Source10:       pyct.1
Source11:       pyct-report.1

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel

BuildRequires:  python3dist(pytest)

%global common_description %{expand:
A utility package that includes:

 1. pyct.cmd: Makes various commands available to other packages. (Currently no
    sophisticated plugin system, just a try import/except in the other
    packages.) The same commands are available from within python. Can either
    add new subcommands to an existing argparse based command if the module has
    an existing command, or create the entire command if the module has no
    existing command. Currently, there are commands for copying examples and
    fetching data.

 2. pyct.build: Provides various commands to help package building, primarily
    as a convenience for project maintainers.}

%description %{common_description}


%package -n python3-pyct
Summary:        %{summary}

# The file pyct/cmd.py contains a progress bar implementation copied (and
# possibly slightly forked?) from an unknown version of
# https://pypi.org/project/clint/. It doesn’t make sense to ask pyct’s upstream
# to support using an external copy of clint, because clint appears to be
# unmaintained upstream.
Provides:       bundled(python3dist(clint))

%description -n python3-pyct %{common_description}


%pyproject_extras_subpkg -n python3-pyct build cmd


%prep
%autosetup -n pyct-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/\bflake8\b/d' setup.py

# Remove shebangs from subcommand modules. These are executable in the source
# tarball, but once installed in site-packages will no longer be executable and
# should be executed indirectly, typically via the “pyct” command. The
# find-then-modify pattern keeps us from discarding mtimes on sources that do
# not need modification.
find pyct -type f -exec \
    gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'


%generate_buildrequires
%pyproject_buildrequires -x build,cmd,tests


%build
%set_build_flags
%pyproject_wheel

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
# Since the documentation uses nbsite, which explicitly targets HTML, it’s
# unlikely we could package satisfactory and guideline-compliant documentation
# even if python3dist(nbsite) were packaged.


%install
%pyproject_install
%pyproject_save_files pyct

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
     '%{SOURCE10}' '%{SOURCE11}'


%check
# Python 3.11: test_report_gives_package_version fails
# https://github.com/pyviz-dev/pyct/issues/94
k="${k-}${k+ and }not test_report_gives_package_version"
# Based loosely on https://github.com/pyviz-dev/pyct/raw/v%%{version}/tox.ini
# _cmd_examples
%pytest -k "${k-}"
(
  set -o errexit
  export PATH="%{buildroot}%{_bindir}:${PATH}"
  export PYTHONPATH='%{buildroot}%{python3_sitelib}'
  %{python3} -c "import pyct; pyct.report('pyct','python','system')"
  # _build_examples
  %{python3} -c "from pyct.build import examples, get_setup_version"
  # _unit
  # (no need to run pytest again!)
  pyct --help
  pyct --version
  pyct report --help
  pyct report pyct python
  %{python3} -m pyct --version
)


%files -n python3-pyct -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE.txt; verify with “rpm -qL -p …”
%doc README.md

%{_bindir}/pyct
%{_mandir}/man1/pyct.1*
%{_mandir}/man1/pyct-*.1*


%changelog
%autochangelog
