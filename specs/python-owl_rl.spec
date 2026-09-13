Name:           python-owl_rl
Version:        7.6.2
Release:        %autorelease
Summary:        A simple implementation of the OWL2 RL Profile
License:        W3C
URL:            https://github.com/RDFLib/OWL-RL
# tarball on pypi does not have scripts
# we have to use github tarball
Source:         https://github.com/RDFLib/OWL-RL/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
A simple implementation of the OWL2 RL Profile, as well as a basic RDFS
inference, on top of RDFLib. Based mechanical forward chaining. The
distribution contains:

* scripts/RDFConvertService: can be used as a CGI script to invoke the
library. It may have to be adapted to the local server setup.
* scripts/owlrl: script that can be run locally to transform a file
into RDF (on the standard output). Run the script with -h to get the
available flags.}

%description %_description


%package -n python3-owl_rl
Summary:        %{summary}

# On PyPI the package is called `owlrl`.
%py_provides python3-owlrl

%description -n python3-owl_rl %_description


%prep
%autosetup -p1 -n OWL-RL-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files owlrl

# Install scripts manually
# https://github.com/RDFLib/OWL-RL/issues/72
install -t %{buildroot}%{_bindir} -D -p -m 0755 \
    scripts/owlrl scripts/RDFConvertService
%py3_shebang_fix %{buildroot}%{_bindir}/*


%check
%pytest -v


%files -n python3-owl_rl -f %{pyproject_files}
%doc README.md
%{_bindir}/owlrl
%{_bindir}/RDFConvertService


%changelog
%autochangelog
