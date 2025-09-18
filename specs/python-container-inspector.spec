%global pypi_name container-inspector
%global pypi_name_with_underscore %(echo "%{pypi_name}" | sed "s/-/_/g")

Name:           python-%{pypi_name}
Version:        33.0.1
Release:        %autorelease
Summary:        Suite of analysis utilities and command line tools for Docker container images

License:        Apache-2.0
URL:            https://github.com/aboutcode-org/container-inspector
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# Disable Sphinx extra theme
Patch:          0001-Revert-Added-docs-server-script-dark-mode-copybutton.patch

BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-reredirects)
BuildRequires:  python3dist(sphinx-rtd-theme)

%global common_description %{expand:
container-inspector is a suite of analysis utilities and command line tools
for Docker images, containers, root filesystems and virtual machine images.

For Docker images, it can process layers and how these relate to each other as
well as Dockerfiles.

container-inspector provides utilities to:

 - identify Docker images in a file system, its layers and the related metadata.
 - given a Docker image, collect and report its metadata.
 - given a Docker image, extract the layers used to rebuild what how a runtime
   rootfs would look.
 - find and parse Dockerfiles.
 - find how Dockerfiles relate to actual images and their layers.
 - given a Docker image, rootfs or Virtual Machime image collect inventories of
   packages and files installed in an image or layer or rootfs
   (implemented using a provided callable)
 - detect the "distro" of a rootfs of image using os-release files (and an
   extensive test suite for these)
 - detect the operating system, architecture}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        Apache-2.0 AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name_with_underscore}

# Generate man pages
export PYTHONPATH=%{buildroot}%{python3_sitelib}
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N --version-string=%{version} -o %{buildroot}%{_mandir}/man1/container_inspector.1 %{buildroot}%{_bindir}/container_inspector


%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CODE_OF_CONDUCT.rst README.rst
%{_bindir}/container_inspector*
%{_mandir}/man1/container_inspector.1*

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog
