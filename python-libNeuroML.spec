%global _description %{expand:
This package provides Python libNeuroML, for working with neuronal models
specified in NeuroML 2 (http://neuroml.org/neuromlv2).  NeuroML provides an
object model for describing neuronal morphologies, ion channels, synapses and
3D network structure.  Documentation is available at
http://readthedocs.org/docs/libneuroml/en/latest/ 
}


Name:           python-libNeuroML
Version:        0.4.1
Release:        %autorelease
Summary:        Python libNeuroML for working with neuronal models specified in NeuroML

License:        BSD
URL:            http://neuroml.org/
Source0:        https://github.com/NeuralEnsemble/libNeuroML/archive/v%{version}/libNeuroML-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-libNeuroML
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-libNeuroML %_description

%package doc
Summary:    Documentation for libNeuroML

%description doc %_description

%prep
%autosetup -n libNeuroML-%{version}

# remove shebang
sed -i '1d' neuroml/nml/nml.py

# correct end of line encoding
sed -i 's/\r$//' neuroml/examples/test_files/tmp2.swc

# Do not try to use pytables snapshots from GitHub (Fedora already carries upstream patches for pytables)
sed -i -e '/^git/ d' -e 's/^tables.*/tables >= 3.3.0/' requirements.txt
# Do not try to install generateds: it is used by upstream to regenerate nml.py from schema but we don't do this in our build
sed -i '/generateds/ d' requirements-dev.txt

%generate_buildrequires
%pyproject_buildrequires -r requirements.txt requirements-dev.txt

%build
%pyproject_wheel

# Do not include sphinx docs since it bundles fonts and js

%install
%pyproject_install
%pyproject_save_files neuroml

%check
%{pytest} -k "not mongodb"

%files -n python3-libNeuroML -f %{pyproject_files}
%license LICENSE
%doc README.md AUTHORS

%files doc
%license LICENSE
%doc README.md AUTHORS
%doc neuroml/examples

%changelog
%autochangelog
