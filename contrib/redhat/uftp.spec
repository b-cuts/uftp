Name:		uftp
Version:	3.6.1
Release:	1%{?dist}
Summary:	Encrypted UDP based FTP metapackage

Group:		System Environment/Daemons
License:	GPL
URL:		http://www.tcnj.edu/~bush/uftp.html
Source0:	%{name}-%{version}.tar
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	openssl-devel
Requires:	openssl

%description
UFTP is an encrypted multicast file transfer program, designed to securely, 
reliably, and efficiently transfer files to multiple receivers simultaneously. 
This is useful for distributing large files to a large number of receivers, 
and is especially useful for data distribution over a satellite link (with 
two way communication), where the inherent delay makes any TCP based 
communication highly inefficient. The multicast encryption scheme is based on 
TLS with extensions to allow multiple receivers to share a common key. UFTP 
also has the capability to communicate over disjoint networks separated by one 
or more firewalls (NAT traversal) and without full end-to-end multicast 
capability (multicast tunneling) through the use of a UFTP proxy server. These 
proxies also provide scalability by aggregating responses from a group of 
receivers. UFTP has been used in the production process of The Wall Street 
Journal to send WSJ pages over satellite to their remote printing plants, and 
other users have used it to send to over 1000 receivers.

%package -n %{name}d
Summary:	Encrypted UPD based FTP daemon with multicast
Group:		System Environment/Daemons
Requires:	openssl

%description -n %{name}d
Provides the program uftpd.  This package is the UFTP receiver.

%package proxy
Summary:	Encrypted UDP based FTP proxy with multicast
Group:		System Environment/Daemons
Requires:	openssl

%description proxy
Provides the program uftpproxyd.  This package provides proxy support for 
the UFTP receiver.

%package utils
Summary:	Encrypted UDP based FTP encryption key management
Group:		System Environment/Daemons
Requires:	openssl

%description utils
Provides the programs uftp_keymgt.  This package provides the utility
for encryption key management.


%prep
%setup -q
#make the install more redhat like
sed -i.redhatify 's|$(DESTDIR)/bin|$(DESTDIR)%{_bindir}|' makefile


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes.txt LICENSE.txt ReadMe.txt
%{_bindir}/uftp
%{_mandir}/man1/uftp.1.gz

%files -n %{name}d
%defattr(-,root,root,-)
%doc Changes.txt LICENSE.txt ReadMe.txt
%{_sbindir}/uftpd
%{_mandir}/man1/uftpd.1.gz

%files proxy
%defattr(-,root,root,-)
%doc Changes.txt LICENSE.txt ReadMe.txt
%{_sbindir}/uftpproxyd
%{_mandir}/man1/uftpproxyd.1.gz

%files utils
%defattr(-,root,root,-)
%doc Changes.txt LICENSE.txt ReadMe.txt
%{_bindir}/uftp_keymgt
%{_mandir}/man1/uftp_keymgt.1.gz


%changelog
* Sun Mar  4 2012 Justin Venus <justin.venus@gmail.com> 3.6.1-1
- adding initial specfile to package uftp
