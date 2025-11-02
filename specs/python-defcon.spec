# Dependency python3dist(fontPens) for “pens” extra is not yet packaged
%bcond pens 0

Name:           python-defcon
Version:        0.12.2
Release:        %autorelease
Summary:        A set of flexible objects for representing UFO data

License:        MIT
URL:            https://github.com/robotools/defcon
Source:         %{pypi_source defcon}

# Temporary downstream workaround for
# https://github.com/robotools/defcon/issues/478,
# https://github.com/fonttools/fonttools/issues/3947, with fonttools 4.60.0.
# The proper fix will be to update F43 to fonttools 4.60.1,
# https://src.fedoraproject.org/rpms/fonttools/pull-request/21.
Patch:          defcon-0.12.2-fonttools-4.60.0.patch

BuildArch:      noarch

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x lxml%{?with_pens:,pens}
BuildOption(install):   -l defcon

BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Defcon is a set of UFO based objects optimized for use in font editing
applications. The objects are built to be lightweight, fast and flexible. The
objects are very bare-bones and they are not meant to be end-all, be-all
objects. Rather, they are meant to provide base functionality so that you can
focus on your application’s behavior, not object observing or maintaining
cached data. Defcon implements UFO3 as described by the UFO font format.}

%description %{_description}


%package -n python3-defcon
Summary:        %{summary}

%description -n python3-defcon %{_description}


%pyproject_extras_subpkg -n python3-defcon lxml %{?with_pens:pens}


%check -a
%pytest


%files -n python3-defcon -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
