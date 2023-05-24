%global _description %{expand:
A simple implementation of the OWL2 RL Profile, as well as a basic RDFS
inference, on top of RDFLib. Based mechanical forward chaining. The
distribution contains:

* scripts/RDFConvertService: can be used as a CGI script to invoke the
library. It may have to be adapted to the local server setup.
* scripts/owlrl: script that can be run locally on to transform a file into RDF
(on the standard output). Run the script with -h to get the available flags.}

Name:           python-owl_rl
Version:        6.0.2
Release:        %autorelease
Summary:        OWL-RL and RDFS based RDF Closure inferencing for Python
License:        W3C
URL:            https://github.com/RDFLib/OWL-RL
Source0:        %{pypi_source owlrl}
# https://github.com/RDFLib/OWL-RL/pull/62
Patch0:         remove_invalid_shebang.patch
BuildArch:      noarch
Obsoletes:      python3-owlrl <= 5.2.1-3

%description %_description


%package -n python3-owl_rl
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  git-core

%description -n python3-owl_rl %_description


%prep
%autosetup -p1 -n owlrl-%{version} -S git


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files owlrl


%check
# test_version_converter needs an internet connection, therefore disabled
%pytest -k 'not cls_maxqc1' \
    --deselect test/test_version_converter.py


%files -n python3-owl_rl -f %{pyproject_files}
%doc README.rst
%{_bindir}/owlrl
%{_bindir}/RDFConvertService


%changelog
%autochangelog
