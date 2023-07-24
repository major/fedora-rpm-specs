%global _description %{expand:
This package provides Python libNeuroML, for working with neuronal models
specified in NeuroML 2 (http://neuroml.org/neuromlv2).  NeuroML provides an
object model for describing neuronal morphologies, ion channels, synapses and
3D network structure.  Documentation is available at
http://readthedocs.org/docs/libneuroml/en/latest/ 
}


Name:           python-libNeuroML
Version:        0.5.3
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

# remove shebangs
for f in "neuroml/nml/nml.py" "neuroml/neuro_lex_ids.py" "neuroml/nml/annotate_nml.py" "neuroml/nml/generatedscollector.py" "neuroml/nml/generatedssupersuper.py" "neuroml/test/test_nml.py" "neuroml/test/test_utils.py"
do
    sed -i '1d'  "${f}"
done

# correct end of line encoding
sed -i 's/\r$//' neuroml/examples/test_files/tmp2.swc

# remove unneeded dev reqs
sed -i -e '/generateds/ d' -e '/flake8$/ d'  -e '/black$/ d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x dev

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
