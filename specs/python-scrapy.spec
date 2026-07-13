%global pypi_name Scrapy
%global pkg_name scrapy
Name:		python-scrapy
Version:	2.17.0
Release:	%autorelease
Summary:	A high-level Python Screen Scraping framework
License:	BSD-3-Clause
URL:		https://scrapy.org
Source:		%{pypi_source %{pkg_name}}
BuildArch:	noarch


%description
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.


%package -n python3-%{pkg_name}
Summary:	%{summary}

%description -n python3-%{pkg_name}
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.





%prep
%autosetup -n %{pkg_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l scrapy


%check
%pyproject_check_import -e 'scrapy.core.downloader.handlers.http2' -e 'scrapy.core.http2.*'


%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc AUTHORS README.rst
%{_bindir}/scrapy


%changelog
%autochangelog
