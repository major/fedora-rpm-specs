# Generated by go2rpm 1.6.0
# Disabled because it needs an ACCOUNT_NAME and ACCOUNT_KEY
%bcond_with check
%global debug_package %{nil}

# https://github.com/Azure/azure-storage-blob-go
%global goipath         github.com/Azure/azure-storage-blob-go
Version:                0.15.0

%gometa

%global common_description %{expand:
Microsoft Azure Blob Storage Library for Go allows you to build applications
that takes advantage of Azure’s scalable cloud storage.

This repository contains the open source Blob SDK for Go.

Features:

Blob Storage:
 - Create/List/Delete Containers
 - Create/Read/List/Update/Delete Block Blobs
 - Create/Read/List/Update/Delete Page Blobs
 - Create/Read/List/Update/Delete Append Blobs}

%global golicenses      LICENSE
%global godocs          BreakingChanges.md ChangeLog.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Microsoft Azure Blob Storage Library for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog