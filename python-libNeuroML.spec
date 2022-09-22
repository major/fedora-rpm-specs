%global _description %{expand:
This package provides Python libNeuroML, for working with neuronal models
specified in NeuroML 2 (http://neuroml.org/neuromlv2).  NeuroML provides an
object model for describing neuronal morphologies, ion channels, synapses and
3D network structure.  Documentation is available at
http://readthedocs.org/docs/libneuroml/en/latest/ 
}


Name:           python-libNeuroML
Version:        0.3.1
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

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.55-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.55-1
- Update to new release
- Use pytest, remove patch

* Thu Feb 18 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.54-1
- Update to latest release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.52-1
- Update to new upstream release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.50-2
- Explicitly BR setuptools

* Sun Jun 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.50-1
- Update to 0.2.50

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.47-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.47-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.47-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.47-1
- Update to 0.2.47
- use github tar since pypi tar does not contain all required files

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-5
- Update to use conditional for spec uniformity

* Fri Oct 26 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-4
- Correct license
- Remove bcond
- Remove hidden buildinfo file
- Correct end of line encoding
- Remove unneeded shebang (https://github.com/NeuralEnsemble/libNeuroML/issues/77)
- Add missing requires

* Thu Oct 25 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-3
- Correct doc build
- Temporarily use bcond

* Thu Oct 25 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-2
- Correct doc sub package name

* Thu Oct 25 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-1
- Initial build
