
%define realname   Data-Dump-Streamer
%define version_orig    2.08-40
%define version   %(echo %{version_orig} | sed s/-/_/)
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    No summary found
Source:     http://www.cpan.org/modules/by-module/Data/%{realname}-%{version_orig}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version_orig}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(B::Deparse)
BuildRequires: perl(B::Utils)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Abbrev)
BuildRequires: perl(Text::Balanced)



%description
no description found

%prep
%setup -q -n %{realname}-%{version_orig}

%build
echo yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


