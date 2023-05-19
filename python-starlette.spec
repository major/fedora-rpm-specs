Name:           python-starlette
Version:        0.27.0
Release:        %autorelease
Summary:        The little ASGI library that shines

# The entire source is BSD-3-Clause, with the possible exception of the
# pre-compiled/minified JavaScript for the Gitter chat app for the
# documentation, which is removed in %%prep anyway.
License:        BSD-3-Clause
URL:            https://www.starlette.io/
Source0:        https://github.com/encode/starlette/archive/%{version}/starlette-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python-starlette-doc < 0.16.0-10

%global common_description %{expand:
Starlette is a lightweight ASGI framework/toolkit, which is ideal for building
async web services in Python.

It is production-ready, and gives you the following:

  • A lightweight, low-complexity HTTP web framework.
  • WebSocket support.
  • In-process background tasks.
  • Startup and shutdown events.
  • Test client built on requests.
  • CORS, GZip, Static Files, Streaming responses.
  • Session and Cookie support.
  • 100%% test coverage.
  • 100%% type annotated codebase.
  • Few hard dependencies.
  • Compatible with asyncio and trio backends.
  • Great overall performance against independant benchmarks.}

%description %{common_description}


%pyproject_extras_subpkg -n python3-starlette full


%package -n     python3-starlette
Summary:        %{summary}

%description -n python3-starlette %{common_description}


%prep
%autosetup -n starlette-%{version}

# Remove Gitter chat app from documentation; it relies on pre-compiled/minified
# JavaScript, which is not acceptable in Fedora. Since we are not building
# documentation, we do this very bluntly:
rm -vrf docs/js

# Produce a filtered version of requirements.txt, which contains testing
# dependencies.
awk '
!NF { next }
$1 == "#" {
  # We do not need the “Optionals”, which correspond to the “full” extra we are
  # already BR’ing; those for “Packaging”, which are for uploading to PyPI; or
  # those for “Documentation”, so long as we are not able to build and package
  # it; but we do need those for “Testing”, except linters, formatters,
  # coverage analysis, and mypy-related dependencies.
  o = $2 !~ /^(Optionals|Documentation|Packaging)$/
  next
}
o {
  # https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
  if ($1 ~ /^(black|coverage|mypy|ruff|types-)/) { next }
  # Drop version pins
  sub(/[>=]=.*$/, "", $0)
  print $0
}
' requirements.txt | tee requirements-filtered.txt


%generate_buildrequires
%pyproject_buildrequires -x full requirements-filtered.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files starlette


%check
# There are new trio.TrioDeprecationWarnings from trio 0.22.0, which would be
# treated as errors; Starlette upstream pins trio 0.21.0 for their CI. We trust
# upstream will encounter and deal with this by the time the deprecated
# functionality is removed.
#
#   E       trio.TrioDeprecationWarning: trio.MultiError is deprecated since
#           Trio 0.22.0; use BaseExceptionGroup (on Python 3.11 and later) or
#           exceptiongroup.BaseExceptionGroup (earlier versions) instead
#           (https://github.com/python-trio/trio/issues/2211)
%pytest -W 'ignore::trio.TrioDeprecationWarning'


%files -n python3-starlette -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
