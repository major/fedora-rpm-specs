Name:           python-docopt
Epoch:          1
Version:        0.6.2
Release:        %autorelease
Summary:        Pythonic argument parser, that will make you smile
License:        MIT
URL:            https://github.com/docopt/docopt
# PyPI tarball doesn't have tests
Source:         %{url}/archive/%{version}/docopt-%{version}.tar.gz
BuildArch:      noarch

# pytest 6.2+ support
Patch:          %{url}/pull/493.patch

%global _description %{expand:
Isn't it awesome how optparse and argparse generate help messages based on your
code?!

Hell no! You know what's awesome? It's when the option parser is generated
based on the beautiful help message that you write yourself!  This way you
don't need to write this stupid repeatable parser-code, and instead can write
only the help message--the way you want it.}


%description %{_description}


%package -n python3-docopt
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-docopt %{_description}


%prep
%autosetup -n docopt-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files docopt


%check
%pytest


%files -n python3-docopt -f %{pyproject_files}
%license LICENSE-MIT
%doc README.rst


%changelog
%autochangelog
