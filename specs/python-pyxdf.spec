Name:           python-pyxdf
Version:        1.17.0
Release:        %autorelease
Summary:        Python package for working with XDF files

License:        BSD-2-Clause
URL:            https://github.com/xdf-modules/pyxdf
Source0:        %{pypi_source pyxdf}
# Required to run some of the tests. This is not mandatory, but why not run all
# the tests we can?  The contents of this archive are licensed (SPDX) MIT, but
# are not installed and do not contribute to the licenses of the binary RPMs.
# The commit hash should be the latest one at the time of the packaged release.
%global ex_commit 387ba537c3a0dd5da2c9a51c578c8f1296e3edeb
%global ex_url https://github.com/xdf-modules/example-files
Source1:        %{ex_url}/archive/%{ex_commit}/example-files-%{ex_commit}.tar.gz

# The package is pure Python and contains no compiled code; however, it has a
# history of endian-dependent test failures, so we make the base package arched
# to ensure the tests run on all architectures (so that any future regressions
# are detected quickly). All binary packages are noarch.
%global debug_package %{nil}
 
BuildRequires:  python3-devel

# See the “dev” dependency group, which also includes unwanted linters etc.
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
pyXDF is a Python importer for XDF files.}

%description %{common_description}


%package -n     python3-pyxdf
Summary:        %{summary}

BuildArch:      noarch

%description -n python3-pyxdf %{common_description}

See python3-pyxdf-examples for the command-line examples (pyxdf.cli).


%package -n     python3-pyxdf-examples
Summary:        %{summary}

BuildArch:      noarch

Requires:       python3-pyxdf = %{version}-%{release}

# This is also a dependency of python3-pyxdf, but we make it explicit since it
# is imported in the example code.
Requires:       %{py3_dist numpy}
# If pylsl (https://pypi.org/project/pylsl/) is ever packaged, we should add a
# manual dependency on it to this subpackage, since pyxdf.cli.playback_lsl
# uses it.

%description -n python3-pyxdf-examples %{common_description}

This package contains the examples (pyxdf.cli). These can be run from the
command line for basic functionality.

  • print_metadata will enable a DEBUG logger to log read messages, then it
    will print basic metadata about each found stream.
      ◦ python3 -m pyxdf.cli.print_metadata -f=/path/to/my.xdf

  • playback_lsl will open an XDF file then replay its data in an infinite
    loop, but using current timestamps. This is useful for prototyping online
    processing.
      ◦ python3 -m pyxdf.cli.playback_lsl /path/to/my.xdf


%prep
%autosetup -n pyxdf-%{version} -p1
%setup -q -n pyxdf-%{version} -T -D -b 1
ln -s ../example-files-%{ex_commit}/ example-files


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pyxdf


%check
%pytest


%files -n python3-pyxdf -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

%exclude %{python3_sitelib}/pyxdf/cli/


%files -n python3-pyxdf-examples
%{python3_sitelib}/pyxdf/cli/


%changelog
%autochangelog
