
Name: rst2pdf
Version: 0.103.1
Release: %autorelease
Summary: Tool for transforming reStructuredText to PDF
License: MIT

URL: https://rst2pdf.org/
Source0: %{pypi_source}

BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildArch: noarch

%description
Tool for transforming reStructuredText to PDF using ReportLab

%prep
%autosetup -n %{name}-%{version} -p 1

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
