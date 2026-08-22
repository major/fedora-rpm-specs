Name: rst2pdf
Version: 0.105
Release: %autorelease
Summary: Tool for transforming reStructuredText to PDF
License: MIT
URL: https://rst2pdf.org/
Source0: %{pypi_source}

# Permit reportlab-5 requirement
# https://github.com/rst2pdf/rst2pdf/pull/1307
Patch0:  rst2pdf-PR1307.patch

BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildArch: noarch

%description
Tool for transforming reStructuredText to PDF using ReportLab

%prep
%autosetup -n %{name}-%{version} -p 1
# Remove version limit for packaging and docutils
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml
sed -i 's/"docutils.*"/"docutils"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files rst2pdf

%files -n %{name} -f %{pyproject_files}
%doc CHANGES.rst Contributors.txt README.rst
%license LICENSE.txt
%{_bindir}/%{name}

%changelog
%autochangelog
