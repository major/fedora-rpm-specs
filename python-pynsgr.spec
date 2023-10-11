%global forgeurl https://github.com/OpenSourceBrain/pynsgr/

%global _description %{expand:
Python interface to the NeuroScience Gateway REST interface, based on pycipres}

Name:           python-pynsgr
Version:        1.0.3
%forgemeta

Release:        %autorelease
Summary:        Interface to the NeuroScience Gateway REST interface
# spdx
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:    noarch

%description %_description

%package -n python3-pynsgr
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  help2man

%description -n python3-pynsgr %_description

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%forgesetup

# remove shebangs
sed -i '1{/^#!/ d}' pynsgr/client.py \
        pynsgr/commands/nsgr_submit.py \
        pynsgr/commands/nsgr_job.py \
        pynsgr/pyjavaproperties.py

# see pyproject-rpm-macros documentation for more forms
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pynsgr

install -d '%{buildroot}%{_mandir}/man1'
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
install -d '%{buildroot}%{_mandir}/man1'
for cmd in nsgr_job nsgr_submit
do
  help2man \
      --no-info \
      --version-string=%{version} \
      --help-option=-h \
      --output="%{buildroot}%{_mandir}/man1/${cmd}.1" \
      "%{buildroot}/%{_bindir}/${cmd}"
  cat %{buildroot}%{_mandir}/man1/${cmd}.1
done


%check
# testing checks for connection to NSG
%pyproject_check_import

%files -n python3-pynsgr -f %{pyproject_files}
%doc README.md CHANGES.txt
%{_bindir}/nsgr_job
%{_bindir}/nsgr_submit
%{_mandir}/man1/nsgr*

%files doc
%license LICENSE
%doc example

%changelog
%autochangelog
