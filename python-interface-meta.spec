%global _description %{expand:
interface_meta provides a convenient way to expose an extensible API with
enforced method signatures and consistent documentation.

This library has been extracted (with some modifications) from omniduct, a
library also principally written by this author, where it was central to the
extensible plugin architecture. It places an emphasis on the functionality
required to create a well-documented extensible plugin system, whereby the act
of subclassing is sufficient to register the plugin and ensure compliance to
the parent API. As such, this library boasts the following features:

- All subclasses of an interface must conform to the parent's API.
- Hierarchical runtime property existence and method signature checking.
  Methods are permitted to add additional optional arguments, but otherwise
  must conform to the API of their parent class (which themselves may have
  extended the API of the interface).
- Subclass definition time hooks (e.g. for registration of subclasses into a
  library of plugins, etc).
- Optional requirement for methods in subclasses to explicity decorate methods
  with an override decorator when replacing methods on an interface, making it
  clearer as to when a class is introducing new methods versus replacing those
  that form the part of the interface API.
- Generation of clear docstrings on implementations that stitches together the
  base interface documentation with any downstream extensions and quirks.
- Support for extracting the quirks documentation for a method from other
  method docstrings, in the event that subclass implementations are done in an
  internal method.
- Compatibility with ABCMeta from the standard library.
}

Name:           python-interface-meta
Version:        1.3.0
Release:        %{autorelease}
Summary:        Provides a convenient way to expose an extensible API

License:        MIT
URL:            https://github.com/matthewwardrop/interface_meta
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-interface-meta
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-interface-meta %_description

%prep
%autosetup -n interface_meta-%{version}
# upstream sets this to 0.0.0
sed -i "s/^version =.*/version = \"%{version}\"/" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files interface_meta

%check
%{pytest}

%files -n python3-interface-meta -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
