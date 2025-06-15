# python-uvloop fails to build with Python 3.14: AttributeError: module
# 'asyncio' has no attribute 'AbstractChildWatcher'
# https://bugzilla.redhat.com/show_bug.cgi?id=2326210
%bcond uvloop 0

Name:           python-hypercorn
Version:        0.17.3
Release:        %autorelease
Summary:        ASGI Server based on Hyper libraries and inspired by Gunicorn

# SPDX
License:        MIT
URL:            https://github.com/pgjones/hypercorn
# PyPI source distributions lack tests, changelog, etc.; use the GitHub archive
Source:         %{url}/archive/%{version}/hypercorn-%{version}.tar.gz

# Downstream-only: patch out coverage analysis
#
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-coverage-analysis.patch
# Remove unnecessary aioquic version limit
# https://github.com/pgjones/hypercorn/pull/267
Patch:          %{url}/pull/267.patch

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -t -x h3,trio%{?with_uvloop:,uvloop}
BuildOption(install):   -L hypercorn

BuildArch:      noarch

BuildRequires:  help2man

%global common_description %{expand:
Hypercorn is an ASGI and WSGI web server based on the sans-io hyper, h11, h2,
and wsproto libraries and inspired by Gunicorn. Hypercorn supports HTTP/1,
HTTP/2, WebSockets (over HTTP/1 and HTTP/2), ASGI, and WSGI specifications.
Hypercorn can utilize asyncio, uvloop, or trio worker types.

Hypercorn can optionally serve the current draft of the HTTP/3 specification
using the aioquic library.}

%description %{common_description}


%package -n python3-hypercorn
Summary:        %{summary}

%description -n python3-hypercorn %{common_description}


%pyproject_extras_subpkg -n python3-hypercorn h3 trio %{?with_uvloop:uvloop}


%install -a
# We must wait until %%install to generate the man page so we can use the
# generated entry point that was installed in the buildroot.
install -d %{buildroot}%{_mandir}/man1
%{py3_test_envvars} help2man \
    --no-info \
    --version-string=%{version} \
    --output=%{buildroot}%{_mandir}/man1/hypercorn.1 \
    %{buildroot}%{_bindir}/hypercorn


%check -a
%tox -- -- -v -k "${k-}"


%files -n python3-hypercorn -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst
%doc README.rst

%{_bindir}/hypercorn
%{_mandir}/man1/hypercorn.1*


%changelog
%autochangelog
