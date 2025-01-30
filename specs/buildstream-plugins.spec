Name:          buildstream-plugins
Summary:       A collection of plugins for the BuildStream project
License:       Apache-2.0
URL:           https://buildstream.build/

BuildArch:     noarch
ExcludeArch:   %{ix86}

Version:       2.4.0
Release:       %autorelease
Source0:       https://github.com/apache/buildstream-plugins/archive/%{version}/buildstream-plugins-%{version}.tar.gz

BuildRequires: python3-devel >= 3.9

Requires:      git
Requires:      lzip
Requires:      patch


%description
A collection of plugins for the BuildStream project


%prep
%autosetup -n %{name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l buildstream_plugins


%files -n %{name} -f %{pyproject_files}
%doc NEWS README.rst

%changelog
%autochangelog
