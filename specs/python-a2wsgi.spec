Name:           python-a2wsgi
Version:        1.10.8
Release:        %autorelease
Summary:        Convert WSGI app to ASGI app or ASGI app to WSGI app
License:        Apache-2.0
URL:            https://github.com/abersheeran/a2wsgi
Source:         %{pypi_source a2wsgi}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-httpx
%if %{undefined rhel}
# starlette is not yet packaged in EPEL
BuildRequires:  python3-starlette
%endif

%global _description %{expand:
Convert WSGI app to ASGI app or ASGI app to WSGI app.  Pure Python.  Only
depend on the standard library.  Compared with other converters, the advantage
is that a2wsgi will not accumulate the requested content or response content in
the memory, so you do not have to worry about the memory limit caused by
a2wsgi.  This problem exists in converters implemented by uvicorn/startlette or
hypercorn.}


%description %_description


%package -n python3-a2wsgi
Summary:        %{summary}


%description -n python3-a2wsgi %_description


%prep
%autosetup -p1 -n a2wsgi-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files a2wsgi

# The pdm build backend includes the license files, but currently the
# pyproject macros don't mark these files as licenses.
sed -e '/LICENSE/ s/^/%%license /' -i %{pyproject_files}


%check
# baize is not yet packaged in Fedora or EPEL
SKIPS='not test_baize_stream_response'

%if %{defined rhel}
# starlette is not yet packaged in EPEL
SKIPS+=' and not test_starlette_stream_response and not test_starlette_base_http_middleware'
%endif

# this test fails with httpx older than 0.28
SKIPS+=' and not test_wsgi_post'

# This project doesn't use the src layout.  Set the import mode during tests to
# ensure we tests the installed Python module, not the local directory.
%pytest --import-mode append --verbose -k "$SKIPS"


%files -n python3-a2wsgi -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
