%global srcname glad2

Name:           python-%{srcname}
Version:        2.0.5
Release:        %autorelease
Summary:        Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator

# Mostly MIT, Apache-2.0 for Khronos and EGL specifications/headers.
License:        MIT and Apache-2.0
URL:            https://github.com/Dav1dde/glad
Source0:        %pypi_source %{srcname}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.


%package -n     %{srcname}
Summary:        %{summary}

Requires:       python3-glad2 = %{version}-%{release}

%description -n %{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%package -n     python3-%{srcname}
Summary:        %{summary}

Conflicts:      python3-glad

%description -n python3-%{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e '1{\@^#!@d}' glad/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files glad

%files -n %{srcname}
%doc README.md
%license LICENSE
%{_bindir}/glad

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog
