# Not building on EPEL 7 as several deps aren't available

%global modname httpbin

%global desc Testing an HTTP Library can become difficult sometimes. RequestBin is \
fantastic for testing POST requests, but doesn't let you control the response. \
This exists to cover all kinds of HTTP scenarios. Additional endpoints are \
being considered. All endpoint responses are JSON-encoded.

Name:           python-%{modname}
Version:        0.10.2
Release:        %autorelease
Summary:        HTTP Request & Response Service, written in Python + Flask

License:        MIT
URL:            https://github.com/psf/httpbin
Source:         https://files.pythonhosted.org/packages/source/h/%{modname}/%{modname}-%{version}.tar.gz
# https://github.com/psf/httpbin/issues/26
# https://github.com/psf/httpbin/pull/32
# Make the dependency on flasgger optional - it has a heavy dep chain
# of its own and is hard to package, and is not needed for using
# httpbin as a library
Patch:          0001-Make-flasgger-dep-optional-26.patch
# https://github.com/psf/httpbin/pull/34
# Replace use of a deprecated Flask config setting
Patch:          0001-Replace-deprecated-JSONIFY_PRETTYPRINT_REGULAR-usage.patch
# https://github.com/psf/httpbin/pull/41
# Fix /bytes endpoint with newer werkzeug versions
Patch:          0001-Fix-bytes-endpoint-with-newer-werkzeug-versions.patch
BuildArch:      noarch

%description
%{desc}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{modname}
%{desc}.

%prep
%autosetup -n %{modname}-%{version} -p1

# Use the Google 'brotli' module, not 'brotlipy'
# When I asked why this uses brotlipy, upstream (Cory Benfield) said:
# "The upstream Brotli module is a hand-coded C extension to Python.
# This has a number of downsides, but the major one is that it ruins
# performance xon PyPy. As an avid user of PyPy, I want something I can
# deploy there. Hence: brotlipy, which uses CFFI."
# For me that's not enough of a reason to bother packaging it.
sed -i -e 's/brotlicffi/brotli/' httpbin/filters.py
sed -i -e 's/brotlicffi/brotli/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

# no need for this to be executable
# https://github.com/psf/httpbin/pull/22
chmod ugo-x httpbin/templates/forms-post.html

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.md AUTHORS

%changelog
%autochangelog
